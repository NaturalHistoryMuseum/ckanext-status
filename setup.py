#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

from setuptools import find_packages, setup

__version__ = '2.1.0'

with open('README.md', 'r') as f:
    __long_description__ = f.read()

setup(
    name='ckanext-status',
    version=__version__,
    description='A CKAN extension that adds a \'status\' bar to the top of the page.',
    long_description=__long_description__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='CKAN data status',
    author='Natural History Museum',
    author_email='data@nhm.ac.uk',
    url='https://github.com/NaturalHistoryMuseum/ckanext-status',
    license='GNU GPLv3',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['ckanext', 'ckanext.status'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points= \
        '''
        [ckan.plugins]
            status=ckanext.status.plugin:StatusPlugin
        ''',
)
