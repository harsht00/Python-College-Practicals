# Password validation to only accept char

try:
    password = input("Enter Password: ")

    if not password.isalpha():
        raise ValueError("Password must contain only characters, no digits or special characters.")

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")

    print("Valid password")

except ValueError as e:
    print(e)