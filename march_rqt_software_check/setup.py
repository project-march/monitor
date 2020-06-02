#!/usr/bin/env python
from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup

d = generate_distutils_setup(
    packages=['march_rqt_software_check', 'march_rqt_software_check.checks'],
    package_dir={'': 'src'},
    scripts=['scripts/march_git_branch_check', 'scripts/march_rqt_software_check'],
)

setup(**d)
