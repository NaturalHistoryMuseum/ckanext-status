import pylons


def status_get_message():
    '''
    Retrieve status message from config file
    :return: status message specified in config file (or None if not specified)
    :rtype: string
    '''

    return pylons.config.get('ckanext.status.message', None)
