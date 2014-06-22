#!/usr/bin/python

from distutils.core import setup

setup(name='Feedme',
      version='1.0',
      description='Rss Podcast Tracker',
      author='Forrest Alvarez',
      py_modules=['feedme'],
      install_require = ['flask', 'feedstail', 'Flask-OAuth', 'pymad'],
     )
