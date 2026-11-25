from threading import Thread
from time import sleep

def even():
    for i in range(2, 11, 2):
        print("Even:", i)
        sleep(1)

def odd():
    for i in range(1, 10, 2):
        print("Odd:", i)
        sleep(1)

t1 = Thread(target=even)
t2 = Thread(target=odd)

t1.start()
t2.start()

t1.join()
t2.join()

print("Number Generation Completed")