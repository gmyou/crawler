import pymongo
from urlparse import urlparse

from crawling_2cpu import get_data as cpu
from crawling_clien import get_data as clien
from crawling_kmug import get_data as kmug
from crawling_tpholic import get_data as tpholic


connection = pymongo.MongoClient("mongodb_server", 27017)

db = connection.crawler
collectionSite  = db.site
collecionArticle  = db.site_article

def insert(domain, data):
      # insert data when it is not exist
    if ( collecionArticle.find({'link':data['link']}).count() == 0 ):
        # TODO {'domain':'', 'count':0, 'update_date':datetime.now()}
        # # data['domain']  = domain
        # # collectionSite.insert()
        collecionArticle.insert(data)
        print domain, data['link'], data['subject']

for data in cpu(), clien(), kmug(), tpholic():
    for d in data:
        parsed_uri = urlparse( d['link'] )
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        # print domain
        insert(domain, d)
