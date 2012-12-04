from urlparse import urlparse

from marteau.fixtures import MarteauFixture
from vaurienclient import Client


class VaurienFixture(object):
    """Setup a vaurien proxy in a particular state, and restore the original
       state at the end of the tests.
    """
    def __init__(self, behavior='dummy', hosts='http://localhost:80',
                 **kwargs):
        self._old_behavior = None
        self.host = host
        self.behavior = behavior
        hosts = hosts.split(',')
        self._clients = [self._get_client(host) for host in hosts]
        self._proxy_args = kwargs

    def _get_client(self, host):
        """Return a vaurien client, or raise a ValueError if "name"
           doesn't exists.
        """
        parts = urlparse(host)
        host, port = parts.netloc.split(':', -1)
        return Client(host, port)

    @classmethod
    def get_name(cls):
        return 'vaurien'

    @classmethod
    def get_arguments(cls):
        return (('host', str, 'http://localhost:80',
                 'host(s) separated by commas'),
                ('behavior', str, 'dummy', 'behavior'))

    def setup(self):
        # first of all, make a call to the proxy to get its current state, in
        # order to replace everythin at the right position in the tearDown
        # method.
        for client in self._clients:
            self._old_behavior = self._client.get_behavior()
            self.set_behavior(self.behavior, **self._proxy_args)

    def tear_down(self):
        """Restore back the previous behavior on the proxy"""
        for client in self._clients:
            self._client.set_behavior(self._old_behavior)


MarteauFixture.register(VaurienFixture)
