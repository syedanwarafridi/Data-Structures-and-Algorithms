"""
In Lock and RLock at a time only one thread is allowed to execute
but sometime our requirements is to execute a particular number of threads at a time.

Semaphore: Helped us to when working multiple threads simatanously
with semaphore there will be max 3 thread can work at time.
Semaphore can be used to limit the access to the shared resources with limited capicity.
"""

from threading import *
import time

obj = Semaphore(3)

def display(name):
    obj.acquire()
    for i in range(5):
        print("Hello")
        print(name)
        time.sleep(4)
    obj.release()
    
t1 = Thread(target=display, args=("Thread-1", ))
t2 = Thread(target=display, args=("Thread-2", ))
t3 = Thread(target=display, args=("Thread-3", ))
t4 = Thread(target=display, args=("Thread-4", ))
t5 = Thread(target=display, args=("Thread-5", ))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()