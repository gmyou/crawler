import pymongo
from crawling_2cpu import get_data

connection = pymongo.MongoClient("mongodb_server", 27017)

db = connection.crawler
collection  = db.site_article

for data in get_data():
    # print data
    collection.insert(data)