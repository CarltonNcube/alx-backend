#!/usr/bin/env python3

"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system using LRU algorithm
    """

    def __init__(self):
        """
        Initialize the LRU cache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, remove the least recently used item (LRU)
                discarded_key = self.queue.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            else:
                if key in self.queue:
                    self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            if key in self.cache_data:
                # Update the usage queue for LRU
                self.queue.remove(key)
                self.queue.append(key)
                return self.cache_data[key]
        return None
