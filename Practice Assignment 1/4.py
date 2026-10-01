#Accept sentence from user and count the vowels in it.
s = input("Enter the sentence: ")
vowels = "aeiouAEIOU"
count = 0

for char in s:
    if char in vowels:
        count += 1

print("Number of vowels in the sentence:", count)