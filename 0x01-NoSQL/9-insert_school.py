#!/usr/bin/env python3
'''function that inserts a new document
'''


def insert_school(mongo_collection, **kwargs):
    '''Return new _id
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
