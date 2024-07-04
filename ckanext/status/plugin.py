#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

from ckan.plugins import SingletonPlugin, implements, interfaces, toolkit
from ckanext.status.lib.helpers import status_get_message, status_enable_html
from ckanext.status import routes
from ckantools.loaders import create_actions, create_auth


class StatusPlugin(SingletonPlugin):
    """
    Provides status bar banner at the top of pages.
    """

    implements(interfaces.IActions, inherit=True)
    implements(interfaces.IAuthFunctions, inherit=True)
    implements(interfaces.IBlueprint)
    implements(interfaces.IConfigurer, inherit=True)
    implements(interfaces.ITemplateHelpers)

    # IActions
    def get_actions(self):
        from ckanext.status.logic import actions

        return create_actions(actions)

    # IAuthFunctions
    def get_auth_functions(self):
        from ckanext.status.logic import auth

        return create_auth(auth)

    # IBlueprint
    def get_blueprint(self):
        """
        IBlueprint hook.
        """
        return routes.blueprints

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
        return {
            'status_get_message': status_get_message,
            'status_enable_html': status_enable_html,
        }
