# Simple program
from threading import Thread

def task():
    print("Thread is running")

# Create thread
t = Thread(target=task)

# Start thread
t.start()

# Waiting for completion
t.join()

print("Main Program Ends")