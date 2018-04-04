#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

from setuptools import setup, find_packages

version = u'0.1'

setup(
    name=u'ckanext-status',
    version=version,
    description=u'Status bar.',
    long_description=u'',
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords=u'',
    author=[u'Alice Butcher', u'Ben Scott'],
    author_email=u'data@nhm.ac.uk',
    url=u'',
    license=u'',
    packages=find_packages(exclude=[u'ez_setup', u'list', u'tests']),
    namespace_packages=[u'ckanext', u'ckanext.status'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points= \
        u'''
            [ckan.plugins]
            status=ckanext.status.plugin:StatusPlugin
        ''',
)
