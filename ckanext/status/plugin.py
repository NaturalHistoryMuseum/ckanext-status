import os
import json
from logging import getLogger
import ckan.plugins as p

log = getLogger(__name__)
ignore_empty = p.toolkit.get_validator('ignore_empty')


class StatusPlugin(p.SingletonPlugin):
    '''
    Provides status bar banner at the top of pages
    '''
    
    # p.implements(p.IConfigurer, inherit=True)
    # p.implements(p.IResourceView, inherit=True)
    #
    # ## IConfigurer
    # def update_config(self, config):
    #     """Add our template directories to the list of available templates"""
    #     p.toolkit.add_template_directory(config, 'theme/templates')
    #     p.toolkit.add_public_directory(config, 'theme/public')
    #     p.toolkit.add_resource('theme/public', 'ckanext-list')
    #
    # def view_template(self, context, data_dict):
    #     return 'list/list_view.html'
    #
    # def form_template(self, context, data_dict):
    #     return 'list/list_form.html'
    #
    # def can_view(self, data_dict):
    #     """
    #     Specify which resources can be viewed by this plugin
    #     @param data_dict:
    #     @return: boolean
    #     """
    #     # Check that we have a datastore for this resource
    #     if data_dict['resource'].get('datastore_active'):
    #         return True
    #     return False
    #
    # ## IResourceView
    # def info(self):
    #     """Return generic info about the plugin"""
    #     return {
    #         'name': 'list',
    #         'title': 'List',
    #         'schema': {
    #             'title_field': [is_datastore_field],
    #             'secondary_title_field': [ignore_empty, is_datastore_field],
    #             'fields': [ignore_empty, is_datastore_field],
    #             'image_field': [ignore_empty, is_datastore_field],
    #         },
    #         'icon': 'list-alt',
    #         'iframed': True,
    #         'filterable': True,
    #         'preview_enabled': True,
    #         'full_page_edit': False
    #     }
    #
    # def setup_template_variables(self, context, data_dict):
    #     """Setup variables available to templates"""
    #     datastore_fields = get_datastore_fields(data_dict['resource']['id'], context)
    #     return {
    #         'resource_json': json.dumps(data_dict['resource']),
    #         'resource_view_json': json.dumps(data_dict['resource_view']),
    #         # Fields - used in the form display options
    #         'fields': [{'text': f, 'value': f} for f in datastore_fields],
    #     }
