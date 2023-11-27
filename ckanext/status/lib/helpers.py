#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

from ckan.plugins import toolkit
import markdown


def status_enable_html():
    return toolkit.asbool(toolkit.config.get('ckanext.status.enable_html', True))


def status_get_message():
    """
    Retrieve status message from config file.

    :returns: status message specified in config file (or None if not specified)
    :rtype: string
    """

    status_message = toolkit.config.get('ckanext.status.message', None)
    if status_message and status_enable_html():
        status_message = markdown.markdown(status_message)
    return status_message
