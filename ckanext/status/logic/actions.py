#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

from ckan.plugins import toolkit, PluginImplementations
from ckanext.status.interfaces import IStatus
from ckantools.decorators import action
from datetime import datetime as dt

ignore_missing = toolkit.get_validator('ignore_missing')

status_help = '''
A list of status reports from across the system.
'''

status_schema = {'state': [ignore_missing, str]}


@action(status_schema, status_help, get=True)
def status_list(state=None):
    status_reports = []

    jobs = toolkit.get_action('job_list')({'ignore_auth': True}, {})
    pending_queues = set([j['queue'] for j in jobs])

    status_reports.append(
        {
            'label': toolkit._('Active queues'),
            'value': len(pending_queues),
            'group': toolkit._('Queues'),
            'help': toolkit._(
                'Number of queues with pending (not actively processing) items'
            ),
            'state': 'good'
            if len(pending_queues) == 0
            else ('ok' if len(pending_queues) < 3 else 'bad'),
        }
    )

    for plugin in PluginImplementations(IStatus):
        status_reports = plugin.modify_status_reports(status_reports)

    if state:
        status_reports = [i for i in status_reports if i['state'] == state]

    return {'reports': status_reports, 'updated_at': dt.now()}
