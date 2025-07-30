# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exceptions import DropItem

import pymongo
import hashlib

class MongoPipeline:
    COLLECTION_NAME = "books"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_database = mongo_db
        # self.client = pymongo.MongoClient(self.mongo_uri)
        # self.db = self.client[self.mongo_database]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE"),
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_database]
        # self.collection = self.db[self.COLLECTION_NAME]

    def close_spider(self, spider):
        self.client.close()

    def compute_item_id(self, item):
        """
        Compute a unique ID for the item based on its content.
        This can be used to avoid duplicates.
        """
        url = item["url"]
        return hashlib.sha256(url.encode("utf-8")).hexdigest()

    def process_item(self, item, spider):
        item_id = self.compute_item_id(item)
        if self.db[self.COLLECTION_NAME].find_one({"_id": item_id}):
            raise DropItem(f"Duplicate item found: {item['title']}")
        else:
            item["_id"] = item_id
            # Insert the item into the MongoDB collection
            self.db[self.COLLECTION_NAME].insert_one(ItemAdapter(item).asdict())
            return item
