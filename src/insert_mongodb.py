import pymongo
from crawling_2cpu import get_data as cpu
from crawling_clien import get_data as clien
from crawling_kmug import get_data as kmug


connection = pymongo.MongoClient("mongodb_server", 27017)

db = connection.crawler
collection  = db.site_article

def insert(data):
      # insert data when it is not exist
    if ( collection.find({'link':data['link']}).count() == 0 ):
        print data['link'], data['subject']
        collection.insert(data)
#           notification

for data in cpu():
    insert(data)

for data in clien():
    insert(data)

for data in kmug():
    insert(data)
