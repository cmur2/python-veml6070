from setuptools import setup

setup(name='veml6070',
      version='1.0.0',
      packages=['veml6070'],

      install_requires=['smbus2'],
      python_requires='>=2.7',

      url='https://dev.mycrobase.de/gitea/cn/python-veml6070',
      author='Christian Nicolai',
      description=' A python library for accessing the VEML6070 digital UV light sensor from Vishay.',
      long_description=open('README.md').read())
