#!/usr/bin/python3

import re
import requests

URL = "https://www.myharvardclassics.com/categories/20120612_1"
TITLE_REGEX = r'main-title.+\>(.+)\<'
EXCERPT_REGEX = r'(Vol\.[^<]+)'

r = requests.get(URL)

titles = re.findall(TITLE_REGEX, r.text)[1:]
excerpts = re.findall(EXCERPT_REGEX, r.text)

for i, t in enumerate(titles):
    print(t, excerpts[i])
