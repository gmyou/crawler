# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re

url = 'http://kmug.co.kr/board/zboard.php'

values = {'id' : 'sale' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
f = urllib2.urlopen(req) 

#f = open('../output/kmug_20150131.html')

soup = BeautifulSoup(f.read())
# print soup

lists = []
article = {}
def printList(su):
        for link in soup.select('table.xectl tr.ctl_list'+str(su)):
            no = link.select('td.ctl_nb')
            print no[0].get_text()
            sbj = link.select('td.ctl_sj')
            if (sbj):
                print sbj[0].select('a')[0].get_text()
                print sbj[0].select('a')[0]['href']
                print sbj[0].select('a')[0]['title']
            name = link.select('td.ctl_name')
            print name[0].get_text()
            hit = link.select('td.ctl_hit')
            print hit[0].get_text()
            date = link.select('td.ctl_date')
            print date[0].get_text()
            print


printList(1)
printList(2)
