# -*- coding: 949 -*-

from bs4 import BeautifulSoup
import sys
import re

f = open("sample.html")

html = f.read()
#print(html)

soup = BeautifulSoup(html)



#Sheet Subject
for string in soup.h1.strings:
    print(repr(string))


#App List
for link in soup.find_all('div'):
    if(link.get('class')=="card-content"):
        print(link.get('data-docid'))
