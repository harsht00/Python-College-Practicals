try:
    num = int(input("Enter the number: "))
    result = 100/num
except:
    print("Num cannot be divided by zero")
else:
    print("Result: ",result)