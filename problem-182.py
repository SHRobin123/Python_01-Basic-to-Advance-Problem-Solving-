#Multiprocessing Example

import multiprocessing
import time

def task1():
    for i in range(5):
        print("Task 1 running:", i)
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2 running:", i)
        time.sleep(1)

if __name__ == "__main__":
    # Creating processes
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    # Starting processes
    p1.start()
    p2.start()

    # Waiting for processes to complete
    p1.join()
    p2.join()

    print("All processes completed")

'''
output:-

Task 1 running: 0
Task 1 running: 1
Task 2 running: 0
Task 2 running: 1
Task 1 running: 2
Task 2 running: 2
Task 1 running: 3
Task 2 running: 3
Task 1 running: 4
Task 2 running: 4
All processes completed
'''