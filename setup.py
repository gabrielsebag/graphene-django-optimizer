#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup

needs_pytest = {"pytest", "test", "ptr"}.intersection(sys.argv)
pytest_runner = ["pytest-runner >=4.0,<5dev"] if needs_pytest else []


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="graphene-django-optimizer-patch",
    version="0.9.1",
    author="Gabriel Sebag",
    author_email="hello@gabrielsebag.com",
    description="Optimize database access inside graphene queries.",
    license="MIT",
    keywords="graphene django optimizer optimize graphql query prefetch select related",
    url="https://github.com/gabrielsebag/graphene-django-optimizer",
    packages=["graphene_django_optimizer"],
    setup_requires=pytest_runner,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.1",
    ],
)
