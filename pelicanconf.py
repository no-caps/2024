#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import re

AUTHOR = 'NOCAPS - Networks and Opinions on Climate Action in the Public Sphere'
SITENAME = 'NOCAPS - Networks and Opinions on Climate Action in the Public Sphere'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [('ICWSM24', 'https://www.icwsm.org/2024/')]

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

# DEFAULT_PAGINATION = False

# # Uncomment following line if you want document-relative URLs when developing
# #RELATIVE_URLS = True

# TEMPLATE_PAGES = {'blog.html': 'blog.html'}
# STATIC_PATHS = ['images', 'extra/CNAME']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# SOCIAL = (('google-plus', 'https://plus.google.com/'),
#           ('linkedin', 'http://www.linkedin.com/in/'),
#           ('githuB', 'https://github.com/'),
#           ('envelope', 'mailto:test@gmail.com'),
#           )

THEME = "BT3-Flat"
OUTPUT_PATH = 'docs/'

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '-', value)
    return value

JINJA_FILTERS = {
    'slugify': slugify,
}