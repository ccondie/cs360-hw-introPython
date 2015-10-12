#!/usr/bin/env python

import requests

print
print "<h1>News</h1>"

page = requests.get('http://news.google.com')
print page.content