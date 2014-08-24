* http://trac.edgewall.org/wiki/TracDev/PluginDevelopment
* http://trac-hacks.org/wiki/DevGuide


## Installation instructions

1. bump the version number in setup.py
2. run `python setup.py bdist_egg`
3. in the Trac admin web interface, under 'General->Plugins', upload the file `dist/GhcCaptcha-<version>-py<python_version>.egg`
4. make sure the new version of the plugin is enabled
5. under 'Spam Filtering->Captcha', select 'GhcCaptcha' as the 'Captcha type' and click 'Apply changes'

## Uninstall

1. Delete all `GhcCaptcha-*-.egg` files from the Trac environment `plugins` directory
2. Restart the Trac server
