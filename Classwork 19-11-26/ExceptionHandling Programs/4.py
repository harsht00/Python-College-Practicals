#one block for multiple exceptions
try:
    num = int(input("Enter the number: "))
    result = 100/num
    print(result)

except(ValueError, ZeroDivisionError):
    print("Invalid operation..")
