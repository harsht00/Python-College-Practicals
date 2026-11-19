# Q6. Write a Python program to create a decorator named
# execution_time() that displays a message before function
# execution, executes the function and displays a message
# after function execution.
# Apply this decorator to a function that calculates factorial.

# Create a decorator named execution_time
def execution_time(func):

    # Create a wrapper function
    def wrapper():

        # Display message before execution
        print("Function Started")

        # Execute the original function
        func()

        # Display message after execution
        print("Function Finished")

    # Return the wrapper function
    return wrapper


# Apply decorator to factorial function
@execution_time
def factorial():

    # Initialize the number
    n = 5

    # Initialize factorial value
    fact = 1

    # Calculate factorial using a loop
    for i in range(1, n + 1):
        fact = fact * i

    # Display factorial result
    print("Factorial =", fact)


# Call the decorated function
factorial()