#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

print
print "<h1>Headlines</h1>"

page = requests.get('http://news.google.com')
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('span',{"class":"titletext"})

for i in results:
	print i.text + "<br>"