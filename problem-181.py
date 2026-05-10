#Multithreading Example

import threading
import time

def task1():
    for i in range(5):
        print("Task 1 running:", i)
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2 running:", i)
        time.sleep(1)

# Creating threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Starting threads
t1.start()
t2.start()

# Waiting for threads to complete
t1.join()
t2.join()

print("All tasks completed")

'''
output:- 

Task 1 running: 0
Task 2 running: 0
Task 1 running: 1
Task 2 running: 1
Task 1 running: 2
Task 2 running: 2
Task 1 running: 3
Task 2 running: 3
Task 1 running: 4
Task 2 running: 4
All tasks completed
'''