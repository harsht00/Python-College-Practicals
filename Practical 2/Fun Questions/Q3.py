#create a list of numbers and strings accepts the values from user, separate the
#list from the maximum number ,display list in descending order.
numbers = []
strings = []

# Accept values from user
for _ in range(5):
    value = input("Enter a number or string: ")
    if value.isdigit():
        numbers.append(int(value))
    else:
        strings.append(value)

# Find the maximum number
max_number = max(numbers)

# Separate the list from the maximum number
filtered_numbers = [n for n in numbers if n != max_number]

# Display the filtered list in descending order
filtered_numbers.sort(reverse=True)
print("Filtered list in descending order:", filtered_numbers)
