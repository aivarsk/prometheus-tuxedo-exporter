import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name="prometheus-tuxedo-exporter",
    version="1.0.0",
    description="A Prometheus exporter of Tuxedo metrics",
    long_description=open("README.rst").read(),
    author="Aivars Kalvans",
    author_email="aivars.kalvans@gmail.com",
    url="https://github.com/aivarsk/prometheus-tuxedo-exporter",
    scripts=["bin/prometheus-tuxedo-exporter.py"],
    install_requires=[
        "tuxedo>=1.0.0",
        "prometheus_client>=0.8.0",
    ],
    license="MIT",
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
    ],
)
