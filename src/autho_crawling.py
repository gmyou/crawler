import urllib
import urllib2
import cookielib
import sys

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

login_url = 'http://tpholic.com/xe/main'
this_url = 'http://tpholic.com/xe/?mid=ibmsellbuy2&category=1521642'
values = {'user_id' : 'user_id',
      'password' : 'user_pwd' }

data = urllib.urlencode(values)
o = opener.open(login_url, data)
f = opener.open(this_url)

the_page = f.read()

print the_page
