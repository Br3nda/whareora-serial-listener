"""Setup file for mysensors package."""
from setuptools import setup

setup(name='pymysensors',
      version='0.5',
      description='Python API for talking to a MySensors gateway',
      url='https://github.com/theolind/pymysensors',
      author='Theodor Lindquist',
      license='MIT',
      install_requires=['pyserial>=3.0'],
      packages=['mysensors'],
      zip_safe=True)
