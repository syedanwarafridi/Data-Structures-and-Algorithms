from threading import Thread

class Example:
    def display(self):
        for i in range(4):
            print("Creating Threads in Class Methods")
            
e1 = Example()

t1 = Thread(target=e1.display)
t1.start()
for i in range(4):
    print("Welcome")
    

