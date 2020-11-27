#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

from ckanext.status.lib.helpers import status_get_message

from ckan.plugins import SingletonPlugin, implements, interfaces, toolkit


class StatusPlugin(SingletonPlugin):
    '''Provides status bar banner at the top of pages'''

    implements(interfaces.IConfigurer, inherit=True)
    implements(interfaces.ITemplateHelpers)

    ## IConfigurer
    def update_config(self, config):
        '''

        :param config:

        '''
        toolkit.add_template_directory(config, u'theme/templates')
        toolkit.add_resource(u'theme/assets', u'ckanext-status')

    ## ITemplateHelpers
    def get_helpers(self):
        ''' '''
        return {
            u'status_get_message': status_get_message
            }
