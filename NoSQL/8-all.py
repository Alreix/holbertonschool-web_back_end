#!/usr/bin/env python3
"""Module that provides a function to list all documents in a collection."""

from pymongo import MongoClient


def list_all(mongo_collection):
    """Return a list of all documents in a collection."""
    return list(mongo_collection.find())