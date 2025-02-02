import threading

class ThreadSafeCache:
    def __init__(self):
        self.cache = {}
        self.lock = threading.Lock()
    
    def put(self, key, value):
        with self.lock:
            self.cache[key] = value
        
    def get(self, key):
        val = ""
        with self.lock:
            val = self.cache.get(key, None)
        return val
    
    def remove(self, key):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
    
    def size(self):
        with self.lock:
            return len(self.cache)
    
    def keys(self):
        return self.cache.keys()