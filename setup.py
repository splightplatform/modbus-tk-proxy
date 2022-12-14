#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Modbus TestKit: Implementation of Modbus protocol in python

 (C)2009 - Luc Jean - luc.jean@gmail.com
 (C)2009 - Apidev - http://www.apidev.fr

 This is distributed under GNU LGPL license, see license.txt
"""

from setuptools import setup
from modbus_tk import VERSION


setup(
    name='modbus_tk_proxy',
    version=VERSION,
    description="Implementation of modbus protocol in python",
    long_description='''
    Modbus Test Kit provides implementation of slave and master for Modbus TCP and RTU
    IT helps to create Modbus app easily with Python
    ''',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications',
        'Topic :: Software Development'
    ],
    keywords='modbus, serial, tcp',
    author='Splight',
    author_email='factory@splight-ae.com',
    maintainer='Splight',
    maintainer_email='factory@splight-ae.com',
    url='https://github.com/splightplatform/modbus-tk/',
    license='LGPL-2.1-or-later',
    packages=['modbus_tk'],
    platforms=["Linux", "Mac OS X", "Win"],
    install_requires=[
        'pyserial>=3.1',
    ],
)
