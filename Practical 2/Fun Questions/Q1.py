#write a program to guess a number hint: use random function.
#Give reward if user guess the number correctly and give hint if user guess the 
#number wrong.

import random
number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("🎉 Correct! You won a reward!")
else:
    print("Wrong guess!")
    
    if guess < number:
        print("Hint: Try a higher number.")
    else:
        print("Hint: Try a lower number.")

print("The correct number was:", number)