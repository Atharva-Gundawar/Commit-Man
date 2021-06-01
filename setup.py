#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'Commit-Man'
DESCRIPTION = 'Official Commit man python package'
URL = 'https://github.com/atharva-Gundawar/commit-man'
EMAIL = 'atharva.n.gundawar@gmail.com'
AUTHOR = 'Atharva Gundawar'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.0.3'

REQUIRED = [
    "datetime", "gitignore_parser", "docopt"
]


here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    # package_dir={'simplepipreqs':
    #              'simplepipreqs'},
    entry_points ={
            'console_scripts': [
                'cm = src.main:main'
            ]
    },
    include_package_data=True,
    install_requires=REQUIRED,
    keywords = 'git commit version-control-system vcs',
    zip_safe = False,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        "Operating System :: OS Independent",
    ]
)