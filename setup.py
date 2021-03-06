#!/usr/bin/env python
'''
Installs the Voxel51 Vision Services Platform SDK.

Copyright 2017-2019, Voxel51, Inc.
voxel51.com
'''
from setuptools import setup, find_packages


setup(
    name="voxel51-platform-sdk",
    version="1.0.0",
    description="Voxel51 Vision Services Platform SDK",
    author="Voxel51, Inc.",
    author_email="support@voxel51.com",
    url="https://github.com/voxel51/platform-sdk",
    license="BSD 4-clause",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "requests>=2.18.4",
    ],
)
