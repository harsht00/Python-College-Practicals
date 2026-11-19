# Q7. Write a Python program using a generator function
# and datetime module to generate dates starting from
# today's date for the next 7 days.

# Import datetime module
import datetime

# Create a generator to generate dates
def generate_dates():

    # Get today's date
    today = datetime.date.today()

    # Run the loop 7 times
    for i in range(7):

        # Generate one date at a time
        yield today + datetime.timedelta(days=i)


# Call the generator and print the dates
for date in generate_dates():
    print(date)