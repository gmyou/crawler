# -*- coding: utf-8 -*-
'''
왜 버전관리가 안되고 있지?
'''


import urllib
import urllib2
from bs4 import BeautifulSoup
import cookielib, requests
import sys
from config import get_account
import re

login_url = 'http://www.cooln.net/login_check'
url = 'http://www.cooln.net/bbs/mart2?sca=%ED%8C%90%EB%A7%A4'

user_id, user_pw = get_account()

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

login_data = urllib.urlencode({'mb_id' : user_id, 'mb_password' : user_pw})
opener.open(login_url, login_data)

f = opener.open(url)

soup = BeautifulSoup(f.read())

datas = []
data = {'subject': '', 'comments': 0, 'writer': '', 'write_date': '', 'price': 0, 'hits': 0, 'link': ''}

def get_data():
    global datas, data

    for tr in soup.find('div', attrs={'class': 'tbl_head01'}).find('table').find('tbody').find_all('tr'):
        subject = tr.find('td', {'class':'td_subject'}).a.get_text().encode('utf-8')
        subjects = subject.split('                    ')
        comment = tr.find('td', {'class':'td_subject'}).find('a', attrs={'class':'win_comment'}).get_text()
        p = re.compile('[0-9]')
        m = p.match(comment)
        if m is None:
            pass
        else:
            data['comments'] = m.group()
        data['subject'] = tr.find('td', {'class':'td_subject'}).a.get_text().encode('utf-8')
        # data['subject'] = subjects[1]
        data['link'] = tr.find('td', {'class':'td_subject'}).a['href']
        data['price'] = tr.find('td', {'class':'td_won'}).get_text()
        if tr.find('td', {'class':'td_name'}).find('span', attrs={'class':'sv_wrap'}) is None:
            pass
        else:
            data['writer'] = tr.find('td', {'class':'td_name'}).find('span', attrs={'class':'sv_wrap'}).a.get_text().encode('utf-8').strip()
        data['write_date'] = tr.find('td', {'class':'td_date'}).get_text()
        data['hits'] = tr.find('td', {'class':'td_hit'}).get_text()
        datas.append(dict(data))

    # for data in datas:
    #     print data['link'], data['subject']

    return datas

# get_data()
