# Q1. Write a Python program to accept a list of numbers
# and find the maximum, minimum, sum and average using
# built-in functions.

# Accept a list of numbers from the user
numbers = list(map(int, input("Enter numbers: ").split()))

# Find the maximum number
print("Maximum:", max(numbers))

# Find the minimum number
print("Minimum:", min(numbers))

# Calculate the sum
print("Sum:", sum(numbers))

# Calculate the average
average = sum(numbers) / len(numbers)
print("Average:", average)