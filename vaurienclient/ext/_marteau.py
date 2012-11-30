from urlparse import urlparse

from marteau.fixtures import MarteauFixture
from vaurienclient import Client


class VaurienFixture(object):
    """Setup a vaurien proxy in a particular state, and restore the original
       state at the end of the tests.
    """

    def __init__(self, config, proxy_name, **kwargs):
        self.config = config
        self._old_behavior = None
        self._client = self._get_client(proxy_name)
        self._proxy_args = kwargs

    def _get_client(self, name):
        """Return a vaurien client, or raise a ValueError if "name"
           doesn't exists.
        """
        parts = urlparse(self._config.get('vaurien-proxies', {})[name])
        host, port = parts.netloc.split(':', -1)
        return Client(host, port)

    def setUp(self):
        # first of all, make a call to the proxy to get its current state, in
        # order to replace everythin at the right position in the tearDown
        # method.
        self._old_behavior = self._client.get_behavior()
        self.set_behavior(**self._proxy_args)

    def tearDown(self):
        """Restore back the previous behavior on the proxy"""
        self._client.set_behavior(self._old_behavior)

MarteauFixture.register(VaurienFixture)
