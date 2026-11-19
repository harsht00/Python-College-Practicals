try:
    print(x)
except NameError:
    print("The x variable is not defined")
except:
    print("Something else went wrong")