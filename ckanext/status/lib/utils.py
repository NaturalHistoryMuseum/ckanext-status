# !/usr/bin/env python
# encoding: utf-8

from cachetools import cached, TTLCache
from ckan.plugins import toolkit


@cached(cache=TTLCache(maxsize=10, ttl=300))
def get_active_queues():
    jobs = toolkit.get_action('job_list')({'ignore_auth': True}, {})
    pending_queues = set([j['queue'] for j in jobs])
    return len(pending_queues)