#!/usr/bin/env python3
"""
LRU caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching system
    """

    def __init__(self):
        """
        Initialization
        used: stores used items, anytime item is called,
        we check for it in the list, if found, delete it from
        the current position then add it to the last position
        """
        super().__init__()
        self.used = []

    def put(self, key, item):
        """
        Add an item in the cache
        if number of items in cache is higher than BaseCaching.MAX_ITEMS,
        discard the least recently used item and print it out then add
        the new item
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        # if key is not in used items, add it else delete it
        # from it's current position then append it to the list
        if key not in self.used:
            self.used.append(key)
        else:
            self.used.append(self.used.pop(self.used.index(key)))

        if len(self.used) > BaseCaching.MAX_ITEMS:
            discard = self.used.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data.keys() and key is not None:
            # remove item from the list and append it to the last postion
            self.used.append(self.used.pop(self.used.index(key)))
            return self.cache_data[key]
        return None
