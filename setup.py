#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the HamBot.

Source:: https://github.com/ampledata/hambot
"""

import os
import sys
import setuptools

__title__ = 'hambot'
__version__ = '1.0.0'
__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    name=__title__,
    version=__version__,
    description='HamBot - Slack Amateur (Ham) Radio Bot',
    author='Greg Albrecht',
    author_email='oss@undef.net',
    packages=['hambot'],
    package_data={'': ['LICENSE']},
    package_dir={'hambot': 'hambot'},
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    url='https://github.com/ampledata/hambot',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'requests >= 2.8.1',
        'slackbot'
    ],
    entry_points={'console_scripts': ['hambot = hambot.cmd:cli']},
    classifiers=[
        'Topic :: Communications :: Ham Radio',
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License'
    ],
    keywords=[
        'Ham Radio'
    ],
)
