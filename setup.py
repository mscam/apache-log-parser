#! /usr/bin/env python

import importlib
from setuptools import setup

version = importlib.import_module('apache_log_parser._version')
__version__ = version.__version__


setup(
    name="apache-log-parser",
    version=__version__,
    author="Rory McCann",
    author_email="rory@technomancy.org",
    packages=['apache_log_parser'],
    install_requires=['user-agents'],
    license='GPLv3+',
    description="Parse lines from an apache log file",
    test_suite='apache_log_parser.tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
