
"""build script for click apps (console scripts)"""
from setuptools import setup

setup(
    name='pathecho',
    version='0.1',
    py_modules=['pathecho', 'userecho', 'hello, 'inout']
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pathecho=pathecho:perform
        userecho=userecho:greet
        hello=hello:hellow
        inout=inout::iocli
    ''',
)
