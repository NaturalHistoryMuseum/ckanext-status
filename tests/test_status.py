#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK
import pytest
from ckan.plugins import toolkit
from ckanext.status.lib.helpers import status_get_message


TEST_MESSAGE = u'this is a test message'


@pytest.mark.ckan_config(u'ckan.plugins', u'status')
@pytest.mark.ckan_config(u'ckanext.status.message', TEST_MESSAGE)
@pytest.mark.usefixtures(u'with_plugins')
def test_helper_gets_message_when_present():
    message = status_get_message()
    assert message == TEST_MESSAGE


@pytest.mark.ckan_config(u'ckan.plugins', u'status')
@pytest.mark.usefixtures(u'with_plugins')
def test_helper_gets_none_when_absent():
    # sanity check
    assert u'ckanext.status.message' not in toolkit.config
    message = status_get_message()
    assert message is None
