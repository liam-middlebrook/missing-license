#!/bin/env python
# -*- coding: utf8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="Missing-License",
    version=version,
    description=("Let GitHub users know if their projects are missing a "
        "license."),
    classifiers=[],
    keywords="python license github",
    author="Liam Middlebrook",
    author_email="liammiddlebrook@gmail.com",
    url="https://github.com/liam-middlebrook/missing-license",
    license="GPLv3",
    packages=find_packages(
    ),
    scripts=[
        "distribute_setup.py",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "PyGithub",
	"click",
    ],
    #TODO: Deal with entry_points
    entry_points="""
    [console_scripts]
    missing-license = Missing_License:create_issue
    """
)
