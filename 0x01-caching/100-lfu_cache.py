#!/usr/bin/env python3
"""
LFU caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFU caching system
    """

    def __init__(self):
        """
        Initialization
        used_list: stores used items and its count, anytime item is called
        """
        self.used_cache = {}
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        if number of items in cache is higher than BaseCaching.MAX_ITEMS,
        discard the least frequently used item and print it out then add
        the new item
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            discard = min(self.used_cache, key=self.used_cache.get)
            self.used_cache.pop(discard)
            self.cache_data.pop(discard)
            print('DISCARD: {}'.format(discard))

        if key in self.used_cache:
            self.used_cache[key] += 1
        else:
            self.used_cache[key] = 0


    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data and key is not None:
            self.used_cache[key] += 1
            return self.cache_data[key]
        return None
