"""
For stoping Race Condition we will be prevent concurrent access.
Lock: 
In python threading module there is class which called "lock", We will be importing this to our program.
Lock technique has two states:
1. Locked: We Will be using the ACQUIRE method which will lock the code until it completes its execution./ The lock has been acquired by one thread and
any thread that makes an attempt to acquire it must wait until it is released.
2. Unlocked: When first thread unlock the code and the next thread acquire it and that makes an attempt.
"""

# from threading import *
# from time import sleep

# mylock = Lock()

# def task(mylock, msg):
#     mylock.acquire()
#     for i in range(5):
#         print(msg)
#     sleep(2)
#     mylock.release()
    
# t1 = Thread(target=task, args=(mylock, "Hello World"))
# t2 = Thread(target=task, args=(mylock, "Welcome"))     
# t1.start()
# t2.start()


from threading import *

lock = Lock()
 
class Bus:
    def __init__(self, name, avaiblable_seats, lock):
        self.name = name
        self.available_seats = avaiblable_seats
        self.lock = lock
        
    def reserve(self, need_seats):
        self.lock.acquire()
        print(f"Available seats are: ", self.available_seats)
        if self.available_seats >= need_seats:
            name = current_thread().name
            print(f"{need_seats} are allocated to {name}")
            self.available_seats -= need_seats
        else:
            print("Sorry! seats are not available")
        self.lock.release()
            
ob1 = Bus("Al Yousaf", 4, lock)

t1 = Thread(target=ob1.reserve, args=(2, ), name="Saeed")
t2 = Thread(target=ob1.reserve, args=(3, ), name="Ahmad")

t1.start()
t2.start()
