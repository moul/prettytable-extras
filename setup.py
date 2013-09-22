#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from prettytable_extras import __version__ as version


setup(
    name='prettytable-extras',
    version=version,
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Topic :: Text Processing',
        ],
    install_requires=[
        'prettytable >= 0.7.2',
        ],
    license="BSD (3 clause)",
    description='An extension to the excellent prettytable Python library',
    author='Manfred Touron',
    author_email='m@42.am',
    url='https://github.com/moul/prettytable-extras',
    py_modules=['prettytable_extras'],
    test_suite='prettytable_extras_test',
    )
