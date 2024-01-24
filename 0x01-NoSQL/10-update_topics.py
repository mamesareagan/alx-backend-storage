#!/usr/bin/env python3
'''Topic change for doc'''


from typing import List
from pymongo import collection


def update_topics(mongo_collection: collection, name, topics):
    '''Change all topics of a school document based on the name
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
