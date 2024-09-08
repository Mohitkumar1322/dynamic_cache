import sys
import os

# Add src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from dynamic_cache_system import DynamicCacheSystem

def test_dynamic_cache_system():
    system = DynamicCacheSystem()
    system.add_cache_level(3, 'LRU')
    system.add_cache_level(2, 'LFU')

    system.put("A", "1")
    system.put("B", "2")
    system.put("C", "3")
    assert system.get("A") == "1"  # Should be from L1
    system.put("D", "4")  # L1 is full, should evict LRU
    assert system.get("C") == "3"  # Should be promoted to L1 from L2

    system.display_cache()

if __name__ == "__main__":
    test_dynamic_cache_system()
    input("Press Enter to exit...")  # Wait for user input before closing
