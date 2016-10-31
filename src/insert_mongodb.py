import pymongo
from urlparse import urlparse
from time import localtime, strftime

from crawling_2cpu import get_data as cpu
from crawling_clien import get_data as clien
from crawling_kmug import get_data as kmug
from crawling_tpholic import get_data as tpholic


connection = pymongo.MongoClient("mongodb_server", 27017)

db = connection.crawler
collectionSite  = db.site
collecionArticle  = db.site_article

def insert(domain, data):
    # upsert siteData when it is not exist
    domainCount = collectionSite.find({'domain': domain}).count()
    articleCount = collecionArticle.find({'link': {'$regex': domain}}).count()
    domainData = {'domain': domain, 'count': articleCount, 'update_date': strftime("%Y-%m-%d %H:%M:%S", localtime())}
    print domainCount, domainData
    if (domainCount == 0):
        collectionSite.insert(domainData)
    else:
        domainData['count'] += 1
        mongoId = collectionSite.find({'domain': domain})
        collectionSite.update({'_id': mongoId[0].get('_id')}, {"$set": domainData}, upsert=False)

    # insert articledData when it is not exist
    if ( collecionArticle.find({'link':data['link']}).count() == 0 ):
        collecionArticle.insert(data)
        print domain, data['link'], data['subject']

for data in cpu(), clien(), kmug(), tpholic():
# for data in cpu(), clien(), tpholic():
    for d in data:
        parsed_uri = urlparse( d['link'] )
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        # print domain
        insert(domain, d)
