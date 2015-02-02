import urllib
import urllib2

url = 'http://tpholic.com/xe/?mid=ibmsellbuy2&category=1521642'
values = {'user_id' : 'hanidrap',
      'password' : 'unicad10' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req) 
the_page = response.read()

print the_page