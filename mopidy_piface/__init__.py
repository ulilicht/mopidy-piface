from __future__ import unicode_literals

import logging
import os


from mopidy import config, ext


__version__ = '0.1.0'

logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = 'Mopidy-Piface'
    ext_name = 'piface'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()

        schema['button1'] = config.String()
        schema['button2'] = config.String()
        schema['button3'] = config.String()
        schema['button4'] = config.String()
        schema['streams'] = config.List()
        
        return schema

    def setup(self, registry):
        # You will typically only implement one of the following things
        # in a single extension.

        from .frontend import FoobarFrontend
        registry.add('frontend', FoobarFrontend)
