# Q4. Write a Python program to calculate employee salary
# using positional, keyword and default arguments.

# Create a function to calculate employee salary
def calculate_salary(basic_salary, bonus=2000):

    # Calculate total salary
    total_salary = basic_salary + bonus

    # Display the salary details
    print("Basic Salary:", basic_salary)
    print("Bonus:", bonus)
    print("Total Salary:", total_salary)


# Call function using positional arguments
calculate_salary(25000, 3000)

# Call function using keyword arguments
calculate_salary(basic_salary=30000, bonus=5000)

# Call function using default argument
calculate_salary(20000)