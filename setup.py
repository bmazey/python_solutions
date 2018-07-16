from setuptools import setup

setup(
   name='exercises',
   version='1.0',
   description='summer 2018 module',
   author='brandon mazey',
   author_email='b.mazey@nyu.edu',
   packages=['challenges', 'exercises'],  # same as name
   install_requires=['bar', 'greek'],  # external packages as dependencies
)
