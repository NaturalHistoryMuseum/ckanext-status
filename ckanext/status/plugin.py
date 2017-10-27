import ckan.plugins as p

from ckanext.status.lib.helpers import status_get_message

class StatusPlugin(p.SingletonPlugin):
    '''
    Provides status bar banner at the top of pages
    '''
    
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.ITemplateHelpers)

    ## IConfigurer
    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'theme/templates')
        p.toolkit.add_public_directory(config, 'theme/public')
        p.toolkit.add_resource('theme/public', 'ckanext-status')

    ## ITemplateHelpers
    def get_helpers(self):
        return {
            'status_get_message': status_get_message
        }
