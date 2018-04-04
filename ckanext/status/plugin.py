#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

import ckan.plugins as p

from ckanext.status.lib.helpers import status_get_message

class StatusPlugin(p.SingletonPlugin):
    '''Provides status bar banner at the top of pages'''
    
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.ITemplateHelpers)

    ## IConfigurer
    def update_config(self, config):
        '''

        :param config: 

        '''
        p.toolkit.add_template_directory(config, u'theme/templates')
        p.toolkit.add_public_directory(config, u'theme/public')
        p.toolkit.add_resource(u'theme/public', u'ckanext-status')

    ## ITemplateHelpers
    def get_helpers(self):
        ''' '''
        return {
            u'status_get_message': status_get_message
        }
