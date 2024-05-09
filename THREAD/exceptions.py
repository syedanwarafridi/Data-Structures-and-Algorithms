from threading import Thread
import time
import threading

"""
Exceptions: If one thread comes with exception errot it will no effect other thread. if only the other thread is not dependent on thread with error.
It will call threaing.excepthook()

"""

def custom_hook(args):
    print("Exception Occured in thread")
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

def display():
    for i in range(4):
        time.sleep(0.1)
        print("Hwllo World" + i)
        
def show():
    for i in range(4):
        print("Hello")

threading.excepthook = custom_hook
t1 = Thread(target=display)
t2 = Thread(target=show)

t1.start()
t2.start()

t1.join()
t2.join()

for i in range(4):
    print("Bye")