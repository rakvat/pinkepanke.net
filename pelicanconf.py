#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = 'Hausprojekt PinkePanke'
SITEURL='https://pinkepanke.net'

PATH = 'content'

FORMATTED_FIELDS = []  # summary is default
PAGES_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_SAVE_AS = ''
ARTICLES_SAVE_AS = ''
ARTICLE_PATHS = ['index', 'news']
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

STATIC_PATHS = ['images', 'css', 'extra']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["year_page_generator"]

NAVIGATION = {
        'aktuelles': 'Aktuelles',
        'denkmal': 'Geschichte und Denkmal',
        'haus': 'Häuser',
        'projekt': 'Projekt',
        'finanzierung': 'Finanzierung',
        'kontakt': 'Kontakt',
}


TIMEZONE = 'Europe/Berlin'
DEFAULT_DATE_FORMAT = '%d.%m.%Y'

LOCALE = ('de')
DEFAULT_LANG = 'de'


TYPOGRIFY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = ()

SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
