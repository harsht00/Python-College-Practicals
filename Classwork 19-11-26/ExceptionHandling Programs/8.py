#Password validation

try:
    password = input("Enter Password: ")

    if password < 8:
        raise ValueError("Password must contain atleast 8 characters..")

    print("valid password")
except ValueError as e:
    print(e)