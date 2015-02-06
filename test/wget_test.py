# -*- coding:utf-8 -*-
import urllib
import urllib2

url = 'http://kmug.co.kr/board/zboard.php'

values = {'id' : 'sale' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req) 
the_page = response.read()

f = open('../resouce/KMug.html', 'r')

f.write(the_page)
