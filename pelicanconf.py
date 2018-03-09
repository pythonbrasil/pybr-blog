#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Python Brasil'
SITENAME = u'Python Brasil Blog'
SITEURL = 'https://blog.pythonbrasil.org.br'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'
THEME = 'themes/pelican-pybr'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
}

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

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
