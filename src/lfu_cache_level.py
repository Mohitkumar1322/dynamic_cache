from collections import defaultdict
from cache_level import CacheLevel

class LFUCacheLevel(CacheLevel):
    def __init__(self, size: int):
        super().__init__(size)
        self.frequency = defaultdict(int)
    
    def evict(self):
        if self.cache:
            min_freq = min(self.frequency.values())
            candidates = [k for k, v in self.frequency.items() if v == min_freq]
            if candidates:
                key_to_evict = candidates[0]
                self.cache.pop(key_to_evict)
                del self.frequency[key_to_evict]
