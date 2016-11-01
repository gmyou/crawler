# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import cookielib, requests
import sys
from config import get_account

login_url = 'http://kbdmania.net/xe/?act=procMemberLogin'
url = 'http://www.kbdmania.net/xe/index.php?mid=market&category=32782'

user_id, user_pw = get_account()

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

login_data = urllib.urlencode({'user_id' : user_id, 'password' : user_pw})
opener.open(login_url, login_data)

f = opener.open(url)

soup = BeautifulSoup(f.read())


datas = []
data = {'number': 0, 'subject': '', 'writer': '', 'write_date': '', 'hits': 0, 'link': '', 'price': ''}

def get_data():
    global datas, data

    for tr in soup.find('table', attrs={'class': 'boardList'}).find_all('tr', attrs={'class': ['bg1', 'bg2']}):
        data['number'] = tr.find('td', {'class':'num'}).get_text()
        data['writer'] = tr.find('td', {'class':'author'}).div.get_text().encode('utf-8').strip()
        data['subject'] = tr.find('td', {'class':'title'}).a.get_text().encode('utf-8').strip()
        data['write_date'] = tr.find('td', {'class':'date'}).get_text()
        data['hits'] = tr.find('td', {'class':'reading'}).get_text()
        data['link'] = url+tr.find('td', {'class':'title'}).a['href'];
        data['price'] = tr.find('td', {'class':''}).get_text().encode('utf-8').strip()
        datas.append(dict(data))

    # for data in datas:
        # print data['link'], data['price'], data['subject']

    return datas

# get_data()
