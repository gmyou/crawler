# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import cookielib, requests
import sys
from config import get_account


login_url = 'https://www.ppomppu.co.kr/zboard/login_check.php'
url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=market&category=3'

user_id, user_pw = get_account()

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

login_data = urllib.urlencode({'user_id' : user_id, 'password' : user_pw})
opener.open(login_url, login_data)

request=urllib2.Request(url, None, headers)
print request.getcode()
sys.exit()
request.add_header('Referer', referer)

f = urllib2.urlopen(request)
print f
sys.exit()

soup = BeautifulSoup(f.read(), from_encoding="euc-kr")
print soup
sys.exit()

datas = []
data = {'number': 0, 'subject': '', 'writer': '', 'write_date': '', 'category': '', 'price': 0, 'link': ''}

def get_data():
    global datas, data

    for tr in soup.find('table', attrs={'id': 'revolution_main_table'}).find('tbody').find_all('tr'):
        data['writer'] = tr.find('td', {'class':'list_name'}).span.get_text().encode('utf-8').strip()
        data['subject'] = tr.find('td', {'class':'list_vspace'}).a.get_text().encode('utf-8').strip()
        data['link'] = url+tr.find('td', {'class':'list_vspace'}).a['href'];
        #TODO data['write_date'] = tr.find('td', {'class':'List_sub_c'}).get_text()
        #TODO data['category'] = tr.find('td', {'class':'List_sub_c'}).get_text()
        data['price'] = tr.find('td', {'class':'List_price'}).get_text()
        datas.append(dict(data))

    for data in datas:
        print data['link'], data['subject']

    return datas

get_data()
