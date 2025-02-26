from threading import Thread, Event
import time

class TrafficLight:
    def __init__(self):
        self.e = Event()
        self.green_light_duration = 5
        self.red_light_duration = 4
        self.cycle = 1

    def SignalController(self):
        
        time.sleep(2)

        for _ in range(self.cycle):
            self.e.set() # Turn light green
            time.sleep(self.green_light_duration)
            self.e.clear() # Turn light red
            time.sleep(self.red_light_duration)
    
    def TrafficResponse(self):
        for _ in range(self.cycle):
            self.e.wait() # Wait for the green light
            while self.e.is_set():
                print("GO AHEAD")
                time.sleep(1)
            print("STOP")
    
    def start1(self):
        t1 = Thread(target=self.SignalController)
        t2 = Thread(target=self.TrafficResponse)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

if __name__=="__main__":
    tarficLight = TrafficLight()
    tarficLight.start()