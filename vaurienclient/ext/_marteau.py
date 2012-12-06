import json
from urlparse import urlparse

from marteau.fixtures import MarteauFixture
from vaurienclient import Client


class VaurienFixture(object):
    """Setup a vaurien proxy in a particular state, and restore the original
       state at the end of the tests.
    """
    def __init__(self, behavior='dummy', hosts='http://localhost:80',
                 behavior_options=None, **kwargs):
        self._old_behavior = None
        self.behavior = behavior
        if behavior_options is None:
            self.behavior_options = {}
        else:
            try:
                self.behavior_options = json.loads(behavior_options)
            except ValueError:
                self.behavior_options = {}

        hosts = hosts.split(',')
        self._clients = [self._get_client(host) for host in hosts]
        self._proxy_args = kwargs
        self._proxy_args.update(self.behavior_options)

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
        return (('hosts', str, 'http://localhost:8000',
                 'host(s) separated by commas'),
                ('behavior', str, 'dummy', 'behavior'),
                ('behavior_options', str, '', 'behavior options (json map)'))

    def setup(self):
        # first of all, make a call to the proxy to get its current state, in
        # order to replace everythin at the right position in the tearDown
        # method.
        for client in self._clients:
            self._old_behavior = client.get_behavior()
            client.set_behavior(self.behavior, **self._proxy_args)

    def tear_down(self):
        """Restore back the previous behavior on the proxy"""
        for client in self._clients:
            client.set_behavior(self._old_behavior)


MarteauFixture.register(VaurienFixture)
