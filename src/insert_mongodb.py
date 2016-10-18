import pymongo
from crawling_2cpu import get_data as cpu
from crawling_clien import get_data as clien
from crawling_kmug import get_data as kmug


connection = pymongo.MongoClient("mongodb_server", 27017)

db = connection.crawler
collection  = db.site_article

for data in cpu():
    print data
    collection.insert(data)

for data in clien():
    print data
    collection.insert(data)

for data in kmug():
    print data
    collection.insert(data)