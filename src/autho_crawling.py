# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib, requests
import sys
# from config import get_account

'''
@param string login_url
@param string login_id
@param string login_pw
@return object opener
'''
def autho(login_url, login_id, login_pw):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    login_data = urllib.urlencode({'user_id' : login_id, 'password' : login_pw})
    opener.open(login_url, login_data)
    return opener


# login_url = 'http://tpholic.com/xe/?act=procMemberLogin'
# this_url = 'http://tpholic.com/xe/?mid=ibmsellbuy2&category=1521642'
#
# user_id, user_pw = get_account()
# print user_id, user_pw
#
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#
# login_data = urllib.urlencode({'user_id' : user_id, 'password' : user_pw})
# opener.open(login_url, login_data)
#
# resp = opener.open(this_url)
# print resp.read()
