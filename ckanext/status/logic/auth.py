#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

from ckantools.decorators import auth
from ckantools.vars import auth_valid


@auth(anon=True)
def status_list(context, data_dict):
    """
    Allow for everyone.
    """
    return auth_valid
