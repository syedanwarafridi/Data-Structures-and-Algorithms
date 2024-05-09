from threading import Thread, current_thread

"""
There are two ways of creating threads:
        1: Using thread class present in thread module.
        2: By extending thread class.
        
Our new thread always will be made by MAIN Thread.
"""

def hellowworld(num):
    print(current_thread().ident)
    for i in range(num):
        print("Hello World!")
        
def display(num):
    print(current_thread().name)
    for i in range(num):
        print("display")
    
t1 = Thread(target=hellowworld, args=(4, ))
t2 = Thread(target=display, args=(4, ))

t1.start()
t2.start()
# display(4)