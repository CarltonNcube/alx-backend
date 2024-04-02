#!/usr/bin/env python3

"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system using LFU algorithm
    """

    def __init__(self):
        """
        Initialize the LFU cache
        """
        super().__init__()
        self.freq_map = {}
        self.min_freq = 0

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, discard least frequently used item
                if len(self.freq_map[self.min_freq]) > 1:
                    del_key = self.freq_map[self.min_freq].pop(0)
                    del self.cache_data[del_key]
                    print("DISCARD:", del_key)
                else:
                    del_key = self.freq_map[self.min_freq].pop()
                    del self.cache_data[del_key]
                    print("DISCARD:", del_key)
            self.cache_data[key] = item
            self.freq_map.setdefault(1, []).append(key)
            self.min_freq = 1

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            if key in self.cache_data:
                self.freq_map[self.min_freq].remove(key)
                if len(self.freq_map[self.min_freq]) == 0:
                    del self.freq_map[self.min_freq]
                    self.min_freq += 1
                self.freq_map.setdefault(self.min_freq, []).append(key)
                return self.cache_data[key]
        return None
