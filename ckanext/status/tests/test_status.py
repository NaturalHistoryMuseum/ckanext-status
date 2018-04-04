#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

import nose
from ckanext.status.lib.helpers import status_get_message

from ckan import plugins
from ckan.plugins import toolkit
from ckan.tests import helpers

eq_ = nose.tools.eq_

test_msg = u'this is a status message'


class TestStatusMessage(object):
    ''' '''

    @classmethod
    def setup_class(cls):
        ''' '''
        cls.app = helpers._get_test_app()
        if not plugins.plugin_loaded(u'status'):
            plugins.load(u'status')

    @classmethod
    def teardown_class(cls):
        ''' '''
        plugins.unload(u'status')

    def _set_msg(self, has_status_message):
        '''

        :param has_status_message: 

        '''
        if has_status_message:
            toolkit.config[u'ckanext.status.message'] = test_msg
        elif u'ckanext.status.message' in toolkit.config:
            del toolkit.config[u'ckanext.status.message']

    def test_helper_gets_message_when_present(self):
        ''' '''
        self._set_msg(has_status_message=True)
        msg = status_get_message()
        eq_(test_msg, msg)

    def test_helper_gets_none_when_absent(self):
        ''' '''
        self._set_msg(has_status_message=False)
        msg = status_get_message()
        eq_(None, msg)
