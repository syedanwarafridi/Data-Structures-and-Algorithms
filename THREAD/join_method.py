"""
    If a thread should wait for another thread.
    then we should go for join method.
"""

from threading import Thread

def display():
    for i in range(5):
        print("display")
        
def show():
    for i in range(5):
        print("Show")
        
t1 = Thread(target=display)
t2 = Thread(target=show)
t1.start()
t1.join() # stop executing t2 until t1 never gets complete
t2.start()

for i in range(5):
    print("Hello World")