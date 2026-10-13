# Take a sentence from the user, split it into words and store 
# them in a list.Print the lonest word.

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)

print("List of words:", words)
print("Longest word:", longest_word)