Vaurien Client
##############

This is a client for `vaurien <http://vaurien.rtfd.org>`_. It's a separate
project to avoid getting all the dependencies of vaurien when you just want to
control it.

It uses `the vaurien's APIs
<https://vaurien.readthedocs.org/en/latest/apis.html>`_ to change the behaviors
on the proxy side.

**vaurienctl** can be used to list the available behaviors, get the current one,
or set it.

Here is a quick demo::

    $ vaurienctl list-behaviors
    delay, error, hang, blackout, dummy

    $ vaurienctl set-behavior blackout
    Behavior changed to "blackout"

    $ vaurienctl get-behavior
    blackout

Using the marteau extension
===========================

*vaurienclient* can be plugged into the marteau mechanism, as a fixture. The
fixture class lives in vaurienclient.ext.marteau.

Here is how you can make it work with a `.marteau.yml` file::

    lookup:
        - vaurienclient.ext.marteau 
    fixtures:
        memcache_delay:
            class: VaurienFixture 
            arguments:
                server: memcache
                behavior: delay
    vaurien-proxies:
        memcache: http://memcache:0123

There are different sections that can be useful here:

* `lookup` tells marteau to load the fixtures that are available on
  `vaurienclient.ext.marteau`.
* fixtures is the list of fixtures. you give them the class to Use (here the
  `VaurienFixture` class, and some arguments.
* And then, the last bit is the list of poxies you want to use.
