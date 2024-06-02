#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *  # noqa


AUTHOR = u'Python Brasil'
SITENAME = u'Python Brasil Blog'
SITEURL = 'https://blog.pythonbrasil.org.br'
RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'
THEME = 'themes/pelican-pybr'

DEFAULT_LANG = 'pt-br'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images']

# Blogroll
LINKS = (
    ('pythonbrasil.org.br', 'https://pythonbrasil.org.br'),
    ('python.org.br', 'https://python.org.br'),
    ('facebook', 'https://www.facebook.com/pythonbrasil'),
    ('twitter', 'https://twitter.com/pythonbrasil'),
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

DEFAULT_PAGINATION = 10

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
