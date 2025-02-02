# Thread Safe Cache 

## Problem Statement

Design and implement a **thread-safe in-memory cache** that allows multiple threads to safely read from and write to the cache concurrently.

## Requirements

1. **Thread Safety:** The cache should be safe for concurrent use. Multiple threads should be able to read from and write to the cache without causing data inconsistencies or corruption.

2. **Basic Cache Operations:**

    - `put(key, value):` Insert or update the value for a given key.
    - `get(key):` Retrieve the value for a given key. If the key doesn't exist, return None.
    - `remove(key):` Remove the entry for a given key from the cache.

3. **Enhancements:**

    - **TTL (Time to Live):** Each key-value pair can have a time-to-live after which it should expire.

    - **Capacity Limit:** Implement an eviction policy (like LRU) if the cache reaches a certain size.