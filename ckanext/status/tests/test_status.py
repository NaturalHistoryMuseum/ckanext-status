import ckan.model as model
import ckan.plugins
import nose
import paste.fixture
import pylons
import pylons.test

from ckanext.status.lib.helpers import status_get_message

eq_ = nose.tools.eq_

test_msg = 'this is a status message'

class TestStatusMessage(object):
    @classmethod
    def setup_class(cls):
        cls.app = paste.fixture.TestApp(pylons.test.pylonsapp)
        ckan.plugins.load('status')

    @classmethod
    def teardown_class(cls):
        ckan.plugins.unload('status')

    def _set_msg(self, has_status_message):
        if has_status_message:
            pylons.config['status_get_message'] = test_msg
        elif 'status_get_message' in pylons.config:
            del pylons.config['status_get_message']

    def test_helper_gets_message_when_present(self):
        self._set_msg(has_status_message = True)
        msg = status_get_message()
        eq_(test_msg, msg)