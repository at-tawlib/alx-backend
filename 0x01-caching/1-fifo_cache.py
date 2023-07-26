#!/usr/bin/env python3
"""
FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching system
    """

    def __init__(self):
        """
        Initialization
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        if number of items in cache is higher than BaseCaching.MAX_ITEMS,
        discard the first item and print it out then add the new item
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            self.cache_data.pop(first_item)
            print('DISCARD: {}'.format(first_item))

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
