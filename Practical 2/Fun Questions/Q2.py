#Consider your name as a string and find all meaningful words or names
# that can be formed using the letters of your name.

name = input("Enter your name: ").lower()

words = ["harsh", "ash", "has", "rash", "arc", "car", "art", "rat"]

for word in words:
    temp = list(name)

    for ch in word:
        if ch in temp:
            temp.remove(ch)
        else:
            break
    else:
        print(word)