#!/usr/bin/env python

from setuptools import setup
from os.path import join, dirname

try:
    long_description = open(join(dirname(__file__), 'README.md')).read()
except Exception:
    long_description = None

setup(
    name='timeline',
    version='0.0.1',
    description='A python library for generating timelines on top of Git',
    author='Kyle Derkacz',
    author_email='kyle@kylederkacz.com',
    url='http://github.com/kylederkacz/timeline',

    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages=['timeline'],
    provides=['timeline'],
    requires=[],
    install_requires=[],
)