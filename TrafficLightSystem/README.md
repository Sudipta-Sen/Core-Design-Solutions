# Simulating a Traffic Light System Using Threads

We will simulate a traffic light system using two threads:

1. **Signal Controller Thread:** This thread is responsible for setting the traffic signal to either red or green. It periodically changes the state of the signal.

2. **Traffic Response Thread:** This thread continuously monitors the signal:

    - When the signal is green, it prints "GO AHEAD" every second.
    - As soon as the signal changes to red, it prints "STOP" once and then waits for the signal to turn green again.

This system runs indefinitely, with both threads working in tandem to simulate real-world traffic light behavior, ensuring that traffic moves when the signal is green and stops when it turns red. The key to this simulation is efficient coordination between the two threads to ensure the proper response based on the current signal state.