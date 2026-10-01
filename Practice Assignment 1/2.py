#Accept two values S and N.Print square of first N numbers starting from S.

S = int(input("Enter the value of S: "))
N = int(input("Enter the value of N: "))

for i in range(S, S + N):
    print(i ** 2)
