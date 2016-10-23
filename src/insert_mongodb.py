import pymongo
from crawling_2cpu import get_data as cpu
from crawling_clien import get_data as clien
from crawling_kmug import get_data as kmug
from crawling_tpholic import get_data as tpholic


connection = pymongo.MongoClient("mongodb_server", 27017)

db = connection.crawler
collection  = db.site_article

def insert(data):
      # insert data when it is not exist
    if ( collection.find({'link':data['link']}).count() == 0 ):
        print data
        collection.insert(data)

for data in cpu():
    insert(data)

for data in clien():
    insert(data)

for data in kmug():
    insert(data)

for data in tpholic():
    insert(data)
