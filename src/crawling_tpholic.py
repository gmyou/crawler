# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import cookielib, requests
import sys
from config import get_account

login_url = 'http://tpholic.com/xe/?act=procMemberLogin'
this_url = 'http://tpholic.com/xe/?mid=ibmsellbuy2&category=1521642'

user_id, user_pw = get_account()

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

login_data = urllib.urlencode({'user_id' : user_id, 'password' : user_pw})
opener.open(login_url, login_data)

f = opener.open(this_url)

soup = BeautifulSoup(f.read())

datas = []
data = {'number': 0, 'subject': '', 'writer': '', 'write_date': '', 'hits': 0, 'link': ''}

def get_data():
    global datas, data

    for tr in soup.find('table', attrs={'class': 'boardList'}).find_all('tr', attrs={'class': 'article'}):
        data['writer'] = tr.find('td', {'class':'author'}).div.get_text().encode('utf-8').strip()
        data['subject'] = tr.find('td', {'class':'title'}).a.get_text().encode('utf-8').strip()
        data['write_date'] = tr.find('td', {'class':'date'}).get_text()
        data['hits'] = tr.find('td', {'class':'reading'}).get_text()
        datas.append(dict(data))

    return datas

# print get_data()
