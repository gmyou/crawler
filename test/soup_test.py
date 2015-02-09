# -*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup
import sys
from symbol import try_stmt
from _ctypes import Array
reload(sys)
sys.setdefaultencoding('utf-8')

soup = BeautifulSoup(open('../resource/KMug.html'))
# print (soup.prettify())

def isArray(obj):
    if (isinstance(obj, Array)):
        return True
    else:
        return False

for link in soup.find_all('tr', attrs={"class": re.compile("^ctl_list")}):
    #id
    #print link.contents[1]
    print link.contents[1].get_text()

    #subject
    try:
        print link.find_all('td', attrs={"class":"ctl_sj"})[0].a.get_text()
    except:
        print 'N/A'
        
    #content
    try:
        print link.find_all('td', attrs={"class":"ctl_sj"})[0].a['title']
    except:
        print 'N/A'
        
    #hit
    try:
        print link.find_all('td', attrs={"class":"ctl_hit"})[0].get_text()
    except:
        print 'N/A'
         
    #date
    try:
        print link.find_all('td', attrs={"class":"ctl_date"})[0].get_text()
    except:
        print 'N/A'
