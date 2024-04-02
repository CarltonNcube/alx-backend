#!/usr/bin/env python3

"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system using LIFO algorithm
    """

    def __init__(self):
        """
        Initialize the LIFO cache
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, remove the last item (LIFO)
                discarded_key = self.stack.pop()
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
