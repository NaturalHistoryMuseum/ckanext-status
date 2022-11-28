#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

from ckan.plugins import SingletonPlugin, implements, interfaces, toolkit
from ckanext.status.lib.helpers import status_get_message


class StatusPlugin(SingletonPlugin):
    """
    Provides status bar banner at the top of pages.
    """

    implements(interfaces.IConfigurer, inherit=True)
    implements(interfaces.ITemplateHelpers)

    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, 'theme/templates')
        toolkit.add_resource('theme/assets', 'ckanext-status')

    # IConfigurer
    def update_config_schema(self, schema):
        ignore_missing = toolkit.get_validator('ignore_missing')
        schema.update(
            {
                'ckanext.status.message': [ignore_missing, str],
            }
        )
        return schema

    # ITemplateHelpers
    def get_helpers(self):
        return {'status_get_message': status_get_message}
