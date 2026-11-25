# Sleep function pauses a thread for a specified time.

from threading import Thread
from time import sleep

def task():
    for i in range(5):
        print(i)
        sleep(1)

t = Thread(target=task)

t.start()