#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 00:07:53 2019

@author: /Kread
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smartgrid", # Replace with your own username
    version="0.0.1",
    author="",
    author_email="",
    description="A python project to manage bidding strategy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucagioacchini/smartgrids",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)