# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['main']
install_requires = \
['bcrypt>=3.2.0,<4.0.0']

setup_kwargs = {
    'name': 'main',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'repl.it user',
    'author_email': 'replituser@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
