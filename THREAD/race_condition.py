"""
Race Condition: Is a bug generated during multi-processing. it occurs because two or three threads are tries to update the same variable, and results are unreliable.
Example: If there are 2 threads running on 1 variable:
suppose we have a variable which name is price and price = 100
now we have 2 threads:
1. Adder Thread :  it will add something to the price varible
2: Subtractor Thread: It will subtract something from the price varibale

When we run this at same the the adder and the subtractor. because of it the result/output can be unreliable.
"""

"""
    We cam solve the race condition with thread synchronization techniques which are followings:
    1. Using Locks
    2. Using R-Lock
    3. Using Semaphorse
"""

from threading import Thread, current_thread
 
class Bus:
    def __init__(self, name, avaiblable_seats):
        self.name = name
        self.available_seats = avaiblable_seats
        
    def reserve(self, need_seats):
        print(f"Available seats are: ", self.available_seats)
        if self.available_seats >= need_seats:
            name = current_thread().name
            print(f"{need_seats} are allocated to {name}")
            self.available_seats -= need_seats
        else:
            print("Sorry! seats are not available")
            
ob1 = Bus("Al Yousaf", 4)

t1 = Thread(target=ob1.reserve, args=(2, ), name="Saeed")
t2 = Thread(target=ob1.reserve, args=(3, ), name="Ahmad")

t1.start()
t2.start()
