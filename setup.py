from setuptools import find_packages, setup

setup(
    name='GhcCaptcha',
    version='0.1',
    url = "https://github.com/thomie/trac-ghccaptcha",
    packages=find_packages(),
    entry_points = {
        'trac.plugins': [
            'ghccaptcha = ghcplugins.ghccaptcha',
        ],
    },
)
