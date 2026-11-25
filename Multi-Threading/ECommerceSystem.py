'''Create three threads to perform:
Product Search
Add to Cart
Payment Processing
Use sleep() to simulate processing time and join() to wait for all tasks.
'''

import threading
import time

# Function for Product Search
def product_search():
    print("Searching products...")
    time.sleep(2)
    print("Products found successfully.")

# Function for Add to Cart
def add_to_cart():
    print("Adding product to cart...")
    time.sleep(3)
    print("Product added to cart successfully.")

# Function for Payment Processing
def payment_processing():
    print("Processing payment...")
    time.sleep(4)
    print("Payment completed successfully.")

print("Online Shopping Started...\n")

# Create Threads
t1 = threading.Thread(target=product_search)
t2 = threading.Thread(target=add_to_cart)
t3 = threading.Thread(target=payment_processing)

# Start Threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to complete
t1.join()
t2.join()
t3.join()

print("\nOrder placed successfully.")
print("Thank you for shopping!")