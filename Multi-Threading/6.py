# Multiple Threads

import threading
import time

def music():
    print("Playing Music")
    time.sleep(3)

def download():
    print("Downloading")
    time.sleep(2)

def chat():
    print("Chatting")
    time.sleep(1)

# Create Threads
t1 = threading.Thread(target=music)
t2 = threading.Thread(target=download)
t3 = threading.Thread(target=chat)

# Start Threads
t1.start()
t2.start()
t3.start()

# Wait for all threads
t1.join()
t2.join()
t3.join()

print("All tasks completed")