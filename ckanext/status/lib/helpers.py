#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

import pylons


def status_get_message():
    '''Retrieve status message from config file


    :returns: status message specified in config file (or None if not specified)

    :rtype: string

    '''

    return pylons.config.get(u'ckanext.status.message', None)
