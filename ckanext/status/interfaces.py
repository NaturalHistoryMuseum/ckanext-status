#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-status
# Created by the Natural History Museum in London, UK

from ckan.plugins import interfaces


class IStatus(interfaces.Interface):
    """
    This interface allows extensions to modify and add status reports for various
    systems.
    """

    def modify_status_reports(self, status_reports):
        """
        Modify the list of items rendered on the status page.

        :param status_reports: items to present on the status page
        :return: the modified list
        """
        return status_reports
