#!/usr/bin/env python3
"""Module that provides a function to insert a document in a collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection and return its new _id."""
    return mongo_collection.insert_one(kwargs).inserted_id
