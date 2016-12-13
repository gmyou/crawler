# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import cookielib, requests
import sys
from config import get_account

login_url = 'https://www.slrclub.com/login/process.php'
url = 'http://www.slrclub.com/bbs/zboard.php?id=used_market&category=1'

user_id, user_pw = get_account()

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

login_data = urllib.urlencode({'user_id' : user_id, 'password' : user_pw})
opener.open(login_url, login_data)

f = opener.open(url)

soup = BeautifulSoup(f.read())


datas = []
data = {'number': 0, 'subject': '', 'writer': '', 'write_date': '', 'recommend': 0, 'hits': 0, 'link': ''}

def get_data():
    global datas, data

    for tr in soup.find('table', attrs={'id': 'bbs_list'}).find('tbody').find_all('tr'):
        if tr.find('td', {'class':'list_num no_att'}) is None: continue

        data['number'] = tr.find('td', {'class':'list_num no_att'}).get_text()
        data['link'] = 'http://www.slrclub.com'+tr.find('td', {'class':'sbj'}).a['href'];
        data['subject'] = tr.find('td', {'class':'sbj'}).a.get_text().encode('utf-8').strip()
        data['writer'] = tr.find('td', {'class':'list_name'}).span.get_text().encode('utf-8').strip()
        data['write_date'] = tr.find('td', {'class':'list_date'}).get_text()
        data['recommend'] = tr.find('td', {'class':'list_vote'}).get_text()
        data['hits'] = tr.find('td', {'class':'list_click'}).get_text()
        datas.append(dict(data))

    # for data in datas:
        # print data['link'], data['subject']

    return datas

# get_data()
