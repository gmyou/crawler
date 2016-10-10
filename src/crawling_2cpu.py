# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import sys

url = 'http://www.2cpu.co.kr/sell'

values = {'bo_table' : 'sell' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
f = urllib2.urlopen(req)

soup = BeautifulSoup(f.read())
data = soup.find('table', attrs={'class': 'table table-condensed table-hover'}).findAll('tr', attrs={'class':'visible-xs'})

for element in data[2:]:
    for td in element.select('td'):
        for child in td.findChildren():
            for a in child.select('a'):
                for span in a.select('span'):
                    print span
        print '------------------------------------------------------'
