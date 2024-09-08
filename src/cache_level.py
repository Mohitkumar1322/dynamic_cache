from collections import OrderedDict
from abc import ABC, abstractmethod

class CacheLevel(ABC):
    def __init__(self, size: int):
        self.size = size
        self.cache = OrderedDict()
    
    @abstractmethod
    def evict(self):
        pass
    
    def get(self, key: str):
        if key in self.cache:
            self.cache.move_to_end(key)  # Move to end to show recent usage
            return self.cache[key]
        return None
    
    def put(self, key: str, value: str):
        if key in self.cache:
            self.cache.move_to_end(key)  # Update existing entry
        elif len(self.cache) >= self.size:
            self.evict()  # Evict if full
        self.cache[key] = value

    def display(self):
        return dict(self.cache)
