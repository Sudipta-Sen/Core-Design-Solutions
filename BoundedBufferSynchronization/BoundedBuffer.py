import threading
import time
import random

class BoundedBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.condition = threading.Condition()
    
    def produce(self, producer_id):
        with self.condition:
            while len(self.buffer)>=self.capacity:
                print(f"Producer-{producer_id} is waiting, since buffer is full")
                self.condition.wait()
            
            item = random.randint(1,100)
            self.buffer.append(item)
            print(f"Producer-{producer_id} produced {item}")
            print(f"Buffer: {self.buffer}")
            time.sleep(2)

            self.condition.notify_all()
    
    def consume(self, consumer_id):
        with self.condition:
            while len(self.buffer)==0:
                print(f"Consumer-{consumer_id} is waiting since buffer is empty")
                self.condition.wait()
            

            item = self.buffer.pop(0)
            print(f"Consumer {consumer_id} consumed item {item}")
            print(f"BUffer: {self.buffer}")
        
def producer(BoundedBufferObj, producer_id):
    while True:
        BoundedBufferObj.produce(producer_id)

def consumer(BoundedBufferObj, consumer_id):
    while True:
        BoundedBufferObj.consume(consumer_id)

if __name__=="__main__":

    BoundedBufferObj = BoundedBuffer(3)

    producer_thread = [threading.Thread(target=producer, args=(BoundedBufferObj, i)) for i in range(3)]
    consumer_thread = [threading.Thread(target=consumer, args=(BoundedBufferObj, i)) for i in range(2)]

    for t in producer_thread+consumer_thread:
        t.start()
    
    for t in producer_thread+consumer_thread:
        t.join()