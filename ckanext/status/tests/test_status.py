#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

import nose
from ckanext.status.lib.helpers import status_get_message
from ckantest.models import TestBase


class TestStatusMessage(TestBase):
    ''' '''
    plugins = [u'status']
    _test_msg = u'this is a status message'

    def tearDown(self):
        self.config.soft_reset()

    def test_helper_gets_message_when_present(self):
        ''' '''
        self.config.update({
                               u'ckanext.status.message': self._test_msg
                               })
        msg = status_get_message()
        nose.tools.assert_equal(self._test_msg, msg)

    def test_helper_gets_none_when_absent(self):
        ''' '''
        # make sure it's not in the config
        self.config.remove([u'ckanext.status.message'])
        assert u'ckanext.status.message' not in self.config.current
        msg = status_get_message()
        nose.tools.assert_equal(None, msg)
