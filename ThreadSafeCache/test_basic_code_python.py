import unittest
from basic_code_python import *
import threading

class TestBasicThreadSafeCode(unittest.TestCase):
    def setUp(self):
        """Initialize a new cache before each test."""
        self.cache = ThreadSafeCache()
    
    def test_single_thread_put_get(self):
        """Test cache operations with a single thread."""
        self.cache.put("key1", "value1")
        self.assertEqual(self.cache.get("key1"), "value1")
    
    def test_single_thread_remove(self):
        """Test cache remove operation with a single thread."""
        self.cache.put("key1", "value1")
        self.cache.remove("key1")
        self.assertIsNone(self.cache.get("key1"))
    
    def test_concurrent_writes(self):
        """Test thread safety with concurrent writes."""
        def writer(thread_id):
            for i in range(100):
                key = f"key-{thread_id}-{i}"
                value = f"value-{thread_id}-{i}"
                self.cache.put(key, value)
        
        threads = [threading.Thread(target=writer, args=(i,)) for i in range(10)]

        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()
        
        for i in range(10):
            for j in range(100):
                key = f"key-{i}-{j}"
                val = f"value-{i}-{j}"
                self.assertEqual(self.cache.get(key), val)
    
    def test_concurrent_reads(self):
        """Test thread safety with concurrent reads."""

        # Populate the cache
        for i in range(100):
            self.cache.put(f"key-{i}", f"value-{i}")
        
        def reader():
            for i in range(100):
                self.assertEqual(self.cache.get(f"key-{i}"), f"value-{i}")
        
        threads = [threading.Thread(target=reader) for _ in range(10)]

        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()
    
    def test_concurrent_read_write(self):
        """Test thread safety with mixed read and write operations."""

        def writer():
            for i in range(100):
                self.cache.put(f"key-write-{i}", f"val-write-{i}")
        
        def reader():
            for i in range(100):
                key = f"key-reader-{i}"
                val = f"val-reader-{i}"
                self.cache.put(key, val)
                self.assertEqual(self.cache.get(key), val)
        
        writer_threads = [threading.Thread(target=writer) for _ in range(10)]
        reader_threads = [threading.Thread(target=reader) for _ in range(10)]

        for thread in writer_threads+reader_threads:
            thread.start()
        
        for thread in writer_threads+reader_threads:
            thread.join()
        
        for i in range(10):
            self.assertEqual(self.cache.get(f"key-write-{i}"), f"val-write-{i}")
            self.assertEqual(self.cache.get(f"key-reader-{i}"), f"val-reader-{i}")
    
    def test_concurrent_remove(self):

        for i in range(100):
            self.cache.put(f"key-{i}", f"val-{i}")
        
        def remover():
            for i in range(100):
                self.cache.remove(f"key-{i}")
        
        threads = [threading.Thread(target=remover) for _ in range(10)]

        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()

        for i in range(100):
            self.assertIsNone(self.cache.get(f"key-{i}"))

if __name__ == '__main__':
    unittest.main()
       
        
