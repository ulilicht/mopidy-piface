import pykka

from mopidy import core


class PifaceFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(PifaceFrontend, self).__init__()
        self.core = core
        str('HELLO WORLD')

    # Your frontend implementation
