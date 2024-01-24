#!/usr/bin/env python3
'''lists all documents in a collection
'''


from pymongo import MongoClient


def list_all(mongo_collection):
    '''Return the list
    '''
    docs = mongo_collection.find({})
    doc_list = list(docs)
    return doc_list
