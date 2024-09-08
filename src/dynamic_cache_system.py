from lru_cache_level import LRUCacheLevel
from lfu_cache_level import LFUCacheLevel

class DynamicCacheSystem:
    def __init__(self):
        self.cache_levels = []
    
    def add_cache_level(self, size: int, eviction_policy: str):
        if eviction_policy == 'LRU':
            self.cache_levels.append(LRUCacheLevel(size))
        elif eviction_policy == 'LFU':
            self.cache_levels.append(LFUCacheLevel(size))
        else:
            raise ValueError("Invalid eviction policy")

    def remove_cache_level(self, level: int):
        if 0 <= level < len(self.cache_levels):
            del self.cache_levels[level]
        else:
            raise IndexError("Cache level out of range")
    
    def get(self, key: str):
        for level in reversed(self.cache_levels):
            value = level.get(key)
            if value is not None:
                for higher_level in reversed(self.cache_levels):
                    if higher_level is not level:
                        higher_level.put(key, value)
                return value
        
        value = self.fetch_from_memory(key)
        self.put(key, value)
        return value
    
    def put(self, key: str, value: str):
        if self.cache_levels:
            self.cache_levels[0].put(key, value)
            for i in range(1, len(self.cache_levels)):
                if self.cache_levels[i].get(key) is not None:
                    self.cache_levels[i].put(key, value)
    
    def display_cache(self):
        for i, level in enumerate(self.cache_levels):
            print(f"L{i+1} Cache:", level.display())

    def fetch_from_memory(self, key: str):
        return f"Value for {key}"
