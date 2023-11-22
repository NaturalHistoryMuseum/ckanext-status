#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK
import pytest
from ckan.plugins import toolkit
from ckanext.status.lib.helpers import status_get_message
import markdown

TEST_MESSAGE = 'this is a test message'
MARKDOWN_TEST_MESSAGE = '_this_ is a test **message**'
HTML_TEST_MESSAGE = '<p><em>this</em> is a test <strong>message</strong></p>'


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.ckan_config('ckan.plugins', 'status')
@pytest.mark.ckan_config('ckanext.status.message', TEST_MESSAGE)
@pytest.mark.ckan_config('ckanext.status.enable_html', False)
@pytest.mark.usefixtures('with_plugins')
def test_helper_gets_message_when_present():
    message = status_get_message()
    assert message == TEST_MESSAGE


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.ckan_config('ckan.plugins', 'status')
@pytest.mark.ckan_config('ckanext.status.message', MARKDOWN_TEST_MESSAGE)
@pytest.mark.ckan_config('ckanext.status.enable_html', True)
@pytest.mark.usefixtures('with_plugins')
def test_helper_parses_markdown_message():
    message = status_get_message()
    assert message == HTML_TEST_MESSAGE


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.ckan_config('ckan.plugins', 'status')
@pytest.mark.usefixtures('with_plugins')
def test_helper_gets_none_when_absent():
    # sanity check
    assert 'ckanext.status.message' not in toolkit.config
    message = status_get_message()
    assert message is None
