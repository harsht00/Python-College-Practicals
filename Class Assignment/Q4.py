#Read a file, split its content into words, amd store them in a list.
# i.Print the total number of words
# ii.Print all unique words.

with open("H:\\abc.txt", 'r') as file:
    content = file.read()
words = content.split()
print("Total number of words:", len(words))
unique_words = set(words)

print("Unique words:", unique_words)