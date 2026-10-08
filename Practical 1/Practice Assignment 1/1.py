# Print the sum of first 10 even numbers

n = 20
sum = 0

for i in range(0, n + 1):
    if i % 2 == 0:
        sum += i

print(sum)