#Read all the lines from file into a list.Print te total number of lines 
# and display the 2nd and 4th line.

with open("H:\\abc.txt", 'r') as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))
print("Second line:", lines[1].strip())
print("Fourth line:", lines[3].strip())