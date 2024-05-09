"""
There are three ways through which we can communicate between 2 threads.
1. Event Class Method: 
2. Queue Object Method: 
3.
"""
import threading
import time
from queue import Queue

######### EVENT Method ###########
# e = threading.Event()

# def task():
#     print("Thread is started")
#     time.sleep(2)
#     e.set() # it will assign True to the Flag Signal
    
# def end():
#     e.wait()
#     if e.is_set():
#         print("Code for destroying session")
        
# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=end)

# t1.start()
# t2.start()

def producer(my_queue):
    print("Producer Running: ")
    n = int(input("Enter the number of students."))
    for i in range(n):
        marks = float(input("Enter Marks"))
        my_queue.put(marks)
    my_queue.put(None)
    print("Producer ends: ")

def consumer(my_queue):
    print("Consumer Running: ")
    while True:
        item = my_queue.get()
        if item is None:
            break
        print(f"Got {item}")
    
    print("Consumer ends: ")

my_queue = Queue()
t1 = threading.Thread(target=producer, args=(my_queue,))
t2 = threading.Thread(target=consumer, args=(my_queue,))

t1.start()
t2.start()