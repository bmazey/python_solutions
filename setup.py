import os
import sys
from setuptools import setup

setup(
   name='exercises',
   version='1.0',
   description='summer 2018 module',
   author='brandon mazey',
   author_email='b.mazey@nyu.edu',
   py_modules=['challenges', 'exercises'],
   # install_requires=['bar', 'greek'],
   # TODO - manage dependencies
)

# added this hack for tests on Travis-CI
sys.path.append(os.getcwd())
