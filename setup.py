#!/usr/bin/env python
# coding=utf-8

import sys
from setuptools import setup, find_packages

if sys.version_info[0] != 3:
    sys.exit('Sorry, only python 3.x is supported')

setup(name='qcloud3_cos_v4',
      version='0.0.20',
      description='python3 sdk for tencent qcloud cos v4.0',
      long_description=open('README.md', 'r').read(),
      license='MIT License',
      install_requires=['requests'],
      author='chenwenbin',
      author_email='chenwenbin1991@126.com',
      url='https://www.xiaodijiaoxue.cn',
      packages=find_packages())
