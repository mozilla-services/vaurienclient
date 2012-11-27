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
