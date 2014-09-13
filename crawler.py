import urllib2
from bs4 import BeautifulSoup
import sys

url = "https://play.google.com/store/apps/collection/topselling_free"
#url = "https://play.google.com/store/apps/collection/topselling_paid"

f = urllib2.urlopen(url)
# f = open('sample.html')

def ConvertKorean(s):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print str(unicode(s))



page = f.read().decode('utf-8', 'ignore')
f.close()

soup = BeautifulSoup(page)

# n = soup.findAll('li', attrs={'class': 'new'})

u = soup.findAll('div', attrs={'class': 'card'})
# print u
for item in u:
	print item['data-docid']
