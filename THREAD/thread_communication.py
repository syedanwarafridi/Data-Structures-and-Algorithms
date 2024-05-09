"""
There are three ways through which we can communicate between 2 threads.
1. Event Class Method: 
2.
3.
"""
import threading
import time

######### EVENT Method ###########
e = threading.Event()

def task():
    print("Thread is started")
    time.sleep(2)
    e.set() # it will assign True to the Flag Signal
    
def end():
    e.wait()
    if e.is_set():
        print("Code for destroying session")
        
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=end)

t1.start()
t2.start()