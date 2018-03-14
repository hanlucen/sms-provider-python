#!/usr/bin/env python

import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'Readme.md')).read()

requires = [
    'requests==2.15.1',
]

includes = (
    'sms_provider',
)

setup(
    name="sms-provider-python",
    version='0.0.1',
    packages=find_packages(),
    install_requires=requires,
    description='a python client for sms',
    long_description=README,
    author="zhumengyuan",
    license="BSD",
    url=""
)
