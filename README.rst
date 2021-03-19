==========================
Prometheus-Tuxedo-Exporter
==========================

A Prometheus exporter of Tuxedo metrics. The code that was too long for the Chapter 6 of my book: 

.. image:: https://ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=180107058X&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=aivarsk-20
    :target: https://amzn.to/3ljktiH

Install
-------

.. code::

  pip3 install prometheus-tuxedo-exporter

Or to install from the local copy:

.. code::

  sudo -E python3 setup.py install

Run
---

The ``prometheus-tuxedo-exporter.py`` can be run as a stand-alone program:

.. code::

  prometheus-tuxedo-exporter.py --port 5555


It can also be run as a Tuxedo server and Tuxedo will take care of starting, stopping and restarting it as a part of the Tuxedo application. For that you will have to add entry like this to ``UBBCONFIG``:

.. code::

  "prometheus-tuxedo-exporter.py" SRVGRP="GROUP1" SRVID=5555
      CLOPT="-- --port 5555"
      MAX=1 MAXGEN=2  GRACE=0 RESTART=Y

Usage
-----

.. code::

  usage: prometheus-tuxedo-exporter.py [-h] --port PORT [--addr ADDR]

  optional arguments:
    -h, --help   show this help message and exit
    --port PORT
    --addr ADDR

The ``--addr`` parameter can be used to specify the network interface to listen on.


Monitoring
----------

Exposed metrics come from `the Management Information Base for core Oracle Tuxedo system <https://docs.oracle.com/cd/E53645_01/tuxedo/docs12cr2/rf5/rf5.html#1803508>`_.


Example:

.. code::

  # HELP tuxedo_numreq_total Number of tpacall or tpcall operations performed from this machine
  # TYPE tuxedo_numreq_total counter
  tuxedo_numreq_total 1149.0
  # HELP tuxedo_numreq_created Number of tpacall or tpcall operations performed from this machine
  # TYPE tuxedo_numreq_created gauge
  tuxedo_numreq_created 1.616197112474299e+09
  # HELP tuxedo_numpost_total Number of tppost operations performed from this machine
  # TYPE tuxedo_numpost_total counter
  tuxedo_numpost_total 0.0
  # HELP tuxedo_numpost_created Number of tppost operations performed from this machine
  # TYPE tuxedo_numpost_created gauge
  tuxedo_numpost_created 1.6161971124743195e+09
  # HELP tuxedo_numtran_total Number of transactions initiated from this machine
  # TYPE tuxedo_numtran_total counter
  tuxedo_numtran_total 0.0
  # HELP tuxedo_numtran_created Number of transactions initiated from this machine
  # TYPE tuxedo_numtran_created gauge
  tuxedo_numtran_created 1.6161971124743354e+09
  # HELP tuxedo_numtranabt_total Number of transactions aborted from this machine
  # TYPE tuxedo_numtranabt_total counter
  tuxedo_numtranabt_total 0.0
  # HELP tuxedo_numtranabt_created Number of transactions aborted from this machine
  # TYPE tuxedo_numtranabt_created gauge
  tuxedo_numtranabt_created 1.6161971124743507e+09
  # HELP tuxedo_numtrancmt_total Number of transactions committed from this machine
  # TYPE tuxedo_numtrancmt_total counter
  tuxedo_numtrancmt_total 0.0
  # HELP tuxedo_numtrancmt_created Number of transactions committed from this machine
  # TYPE tuxedo_numtrancmt_created gauge
  tuxedo_numtrancmt_created 1.6161971124743652e+09
