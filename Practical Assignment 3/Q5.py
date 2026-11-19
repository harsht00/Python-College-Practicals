# Q5. Write a Python program to demonstrate map(),
# filter() and reduce() functions on a list of numbers.

# Import reduce from functools
from functools import reduce

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map: Calculate square of each number
squares = list(map(lambda x: x * x, numbers))

# Filter: Get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce: Calculate sum of all numbers
total = reduce(lambda a, b: a + b, numbers)

# Display the results
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Sum:", total)