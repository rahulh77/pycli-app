from setuptools import setup

setup(
    name='cliapp',
    version='1.0',
    py_modules=['cliapp'],
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        hello=hello:cli
    '''
)