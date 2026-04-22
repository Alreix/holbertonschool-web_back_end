#!/usr/bin/env python3
"""Module that provides a function to update school topics."""


def update_topics(mongo_collection, name, topics):
    """Change all topics of school documents based on the school name."""
    mongo_collection.update_many(
        {"name": name},
        { "$set": {"topics": topics}}
    )
