#!/usr/bin/env python3
import asyncio
import sys
import argparse

import tuxedo as t
from prometheus_client import Counter, start_http_server
from prometheus_client.registry import REGISTRY

numreq = Counter(
    "tuxedo_numreq",
    "Number of tpacall or tpcall operations performed from this machine",
)
numpost = Counter(
    "tuxedo_numpost", "Number of tppost operations performed from this machine"
)
numtran = Counter(
    "tuxedo_numtran", "Number of transactions initiated from this machine"
)
numtranabt = Counter(
    "tuxedo_numtranabt", "Number of transactions aborted from this machine"
)
numtrancmt = Counter(
    "tuxedo_numtrancmt", "Number of transactions committed from this machine"
)
numenqueue = Counter(
    "tuxedo_numenqueue", "Number of tpenqueue operations performed from this machine"
)
numdequeue = Counter(
    "tuxedo_numdequeue", "Number of tpdequeue operations performed from this machine"
)


def collect_machine():
    machine = t.tpadmcall(
        {
            "TA_CLASS": "T_MACHINE",
            "TA_OPERATION": "GET",
            "TA_FLAGS": t.MIB_LOCAL,
        }
    ).data
    numreq._value.set(machine["TA_NUMREQ"][0])
    numpost._value.set(machine["TA_NUMPOST"][0])
    numtran._value.set(machine["TA_NUMTRAN"][0])
    numtranabt._value.set(machine["TA_NUMTRANABT"][0])
    numtrancmt._value.set(machine["TA_NUMTRANCMT"][0])
    numenqueue._value.set(machine["TA_NUMENQUEUE"][0])
    numdequeue._value.set(machine["TA_NUMDEQUEUE"][0])


class TuxedoCollector:
    def collect(self):
        collect_machine()
        yield from REGISTRY.collect()


def prometheus(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", dest="port", required=True)
    parser.add_argument("--addr", dest="addr", default="")
    args = parser.parse_args(argv)
    start_http_server(int(args.port), args.addr, TuxedoCollector())


def run_client():
    t.tpinit(cltname="tpsysop")
    prometheus(sys.argv[1:])

    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    finally:
        loop.close()


class Server:
    def tpsvrinit(self, argv):
        if "--" not in sys.argv:
            t.userlog("Missing CLOPT arguments")
            return -1

        prometheus(sys.argv[sys.argv.index("--") + 1 :])
        return 0


def run_server():
    t.run(Server(), sys.argv)


if __name__ == "__main__":
    for opt in ("-g", "-i", "-u", "-U", "-m"):
        if opt not in sys.argv:
            run_client()
            break
    else:
        run_server()
