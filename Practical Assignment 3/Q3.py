# Q3. Write a Python program using math and random modules
# to generate a random number and calculate its square root.

# Import math and random modules
import math
import random

# Generate a random number between 1 and 100
num = random.randint(1, 100)
print("Random Number:", num)

# Calculate the square root
print("Square Root:", math.sqrt(num))