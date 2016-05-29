from setuptools import setup

setup(name='veml6070',
      version='1.0',
      url='http://github.com/cmur2/python-veml6070',
      author='Christian Nicolai',
      description=' A python library for accessing the VEML6070 digital UV light sensor from Vishay.',
      packages=['veml6070'],
      long_description=open('README.md').read(),
      requires=['python (>= 2.7)', 'smbus (>= 0.4.1)'],
      install_requires=['smbus-cffi'])