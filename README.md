Single file plugin
* http://trac.edgewall.org/wiki/TracDev/PluginDevelopment
* http://trac-hacks.org/wiki/DevGuide#MetadataforSingle-FilePlugins


## Installation instructions

In the Trac admin web interface:

1. under 'General->Plugins', upload the file `ghccaptcha.py`
2. make sure the new plugin is enabled
3. under 'Spam Filtering->Captcha', select 'GhcCaptcha' as the 'Captcha type' and click 'Apply changes'


## Installing a new version

Since the Trac admin web interface doesn't seem to support updating a single file plugin, instead:

1. overwrite existing `ghccaptcha.py` in the Trac environment `plugins` directory
2. restart the Trac server
