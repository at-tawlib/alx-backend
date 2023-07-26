#!/usr/bin/env python3
"""
LIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO caching system
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
        discard the last item and print it out then add the new item
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                and key not in self.cache_data.keys():
            discard = self.cache_data.popitem()
            print('DISCARD: {}'.format(discard[0]))

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
