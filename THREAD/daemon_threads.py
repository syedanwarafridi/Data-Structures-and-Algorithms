"""
Daemon Threads: Which supports automatic Closing

Non Daemon Threads: Program will not terminate until all non-darmon threads gets completed.
Daemon Threads: When all daemon threads gets terminated, automatically daemon threads also gets terminated. daemon threads run continously in background and provide support to other non-daemon thread.

Use of Daemon Threads: Daemon threads are often used for tasks such as monitoring, beckground services, or cleanup operations.

"""

# from threading import *
# obj = current_thread()

# print(obj.daemon) # Main thread is not a Daemon Thread

from threading import *
import time

def display():
    for i in range(10):
        print("Teaching Session: ", i, "\n")
        time.sleep(0.7)
        
t1 = Thread(target=display)
t1.daemon = True
t1.start()


print("Exam is Start!")
print("Exam is over.")