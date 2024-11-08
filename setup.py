# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from os import path as os_path

packages = find_packages(exclude=['tests*'])

# Package meta-data.
DESCRIPTION = 'Python client for RePec API'

# Short/long description.
here = os_path.abspath(os_path.dirname(__file__))
try:
    with open(os_path.join(here, 'README.md'), 'r', encoding='utf-8') as file:
        long_desc = '\n' + file.read()
except FileNotFoundError:
    long_desc = DESCRIPTION

setup(
    name='pyrepec',
    version='0.1.7',
    keywords='api client repec',
    description=DESCRIPTION,
    packages=packages,
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'requests'
    ],
)
