"""build script for click apps (console scripts)"""
from setuptools import setup

setup(
    name='xmenu',
    version='0.1',
    py_modules=['xmenu'],
    install_requires=[
        'Click',
        'sh'
    ],
    entry_points='''
        [console_scripts]
        xmenu=xmenu:xdomenu
    ''',
)
