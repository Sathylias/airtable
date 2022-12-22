#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Airtable API's setup.py
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="airtable",
    version="0.0.1",
    author="Maxime Daraiche",
    author_email="max@techstew.dev",
    description="Airtable API Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sathylias/airtable",
    packages=find_packages(),

classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
    python_requires='>=3.6',
)
