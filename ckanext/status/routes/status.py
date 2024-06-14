#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

import itertools

from flask import Blueprint

from ckan.plugins import toolkit

blueprint = Blueprint(name='status', import_name=__name__, url_prefix='/status')


@blueprint.route('/')
def index():
    """
    Renders an HTML page showing status items.
    """
    status_response = toolkit.get_action('status_list')({}, {})

    grouped_reports = {
        k: list(v)
        for k, v in itertools.groupby(
            sorted(status_response['reports'], key=lambda x: x.get('group', '_root')),
            key=lambda x: x.get('group', '_root'),
        )
    }

    return toolkit.render(
        'status/index.html',
        extra_vars={
            'reports': grouped_reports,
            'updated_at': status_response['updated_at'],
        },
    )
