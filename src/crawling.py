# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re

'''
url = 'http://kmug.co.kr/board/zboard.php'

values = {'id' : 'sale' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req) 
the_page = response.read()

print the_page
'''

f = open('../output/kmug_20150131.html')
soup = BeautifulSoup(f.read())
# print soup

lists = []
article = {}
for tr in soup.find_all("tr", attrs={"class": "ctl_list1"}):
    #aid : article id, pid : present number
    td = tr.contents[1]
    print td
    m = re.compile(r"\b(\d+)\b")
    ids = m.findall(str(td))
    article['aid'] = ids[0]
    article['pid'] = ids[1]
    print article
    lists.append(article)
    break

for l in lists:
    print l