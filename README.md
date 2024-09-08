# Dynamic Multilevel Caching System

## Overview

This project implements a dynamic multilevel caching system that supports multiple cache levels with configurable sizes and eviction policies. It efficiently manages data across these cache levels using either Least Recently Used (LRU) or Least Frequently Used (LFU) eviction strategies. 

## Approach

### Design Decisions

1. **Dynamic Cache Levels:**
   - The system allows adding and removing cache levels at runtime. Each cache level can have a distinct size and eviction policy.
   - Data is retrieved from the highest-priority cache level first. If not found, it is fetched from lower levels or the main memory.

2. **Eviction Policies:**
   - **Least Recently Used (LRU):** Evicts the least recently accessed item.
   - **Least Frequently Used (LFU):** Evicts the least frequently accessed item.
   - Both policies ensure that the cache remains optimal in terms of space utilization and performance.

3. **Concurrency (Bonus):**
   - Implemented thread-safe operations for concurrent access to the cache system to handle real-world multi-threaded scenarios.

4. **Data Management:**
   - When data is retrieved from a lower cache level, it is promoted to higher levels, and when new data is inserted, it is always added to the L1 cache.

## How To run:
1) Clone the repo
2) go to dynamic-cache-system and then go to tests folder there run a script python test_cache_system.py


### Files Explained

- **`src/`**: Contains the core implementation of the caching system.
  - **`__init__.py`**: Marks the directory as a package.
  - **`cache_level.py`**: Defines the base class for cache levels.
  - **`lru_cache_level.py`**: Contains the implementation of LRU cache level.
  - **`lfu_cache_level.py`**: Contains the implementation of LFU cache level.
  - **`dynamic_cache_system.py`**: Main class that manages multiple cache levels and provides the interface for cache operations.

- **`tests/`**: Contains unit tests for the caching system.
  - **`__init__.py`**: Marks the directory as a package.
  - **`test_cache_system.py`**: Test cases for validating the functionality of the cache system.

## Key Decisions

- **Dynamic Management:** The system allows dynamic adjustment of cache levels to accommodate varying requirements.
- **In-Memory Storage:** Data is stored in memory to ensure fast access and manipulation, as specified in the project requirements.
- **Modular Code:** Separated responsibilities into different files and classes for better maintainability and readability.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
