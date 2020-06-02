#!/usr/bin/env python
from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup

d = generate_distutils_setup(
    packages=['march_rqt_note_taker'],
    package_dir={'': 'src'},
    scripts=['scripts/march_rqt_note_taker'],
)

setup(**d)
