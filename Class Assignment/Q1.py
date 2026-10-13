# Write a program to read a file and count how many voels are present in 
# its content.

def count_vowels_in_file(file_path):
    vowels = "aeiouAEIOU"
    count = 0

    with open(file_path, 'r') as file:
        content = file.read()
        for char in content:
            if char in vowels:
                count += 1
    return count
print(count_vowels_in_file("H:\\abc.txt"))
