from cache_level import CacheLevel

class LRUCacheLevel(CacheLevel):
    def evict(self):
        if self.cache:
            self.cache.popitem(last=False)  # Remove the least recently used item
