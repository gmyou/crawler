# -*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

soup = BeautifulSoup(open('../resource/KMug.html'))
# print (soup.prettify())

for link in soup.find_all('tr', attrs={"class": re.compile("^ctl_list")}):
    #id
    #print link.contents[1]
    print link.contents[1].get_text()
    #subject
    print link.find_all('td', attrs={"class":"ctl_sj"})[0].a.get_text()
    #content
    print link.find_all('td', attrs={"class":"ctl_sj"})[0].a['title']
    #hit
    print link.find_all('td', attrs={"class":"ctl_hit"})[0].get_text()
    #date
    print link.find_all('td', attrs={"class":"ctl_date"})[0].get_text()
