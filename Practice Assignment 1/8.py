#print following pattern
#   @
#  ***
# @@@@@
#*******
n = 4
for i in range(n):
    if i == 0:
        print(" " * (n - i - 1) + "@")
    elif i == 1:
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    elif i == 2:
        print(" " * (n - i - 1) + "@" * (2 * i + 1))
    else:
        print("*" * (2 * i + 1))