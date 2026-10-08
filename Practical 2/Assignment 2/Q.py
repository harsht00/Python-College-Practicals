#Create a list of 10 numbers , print the sum of last 4 elements 
# of the list , find out the differnence between max and min element 
# of the list , insert a number in a list at 6th position this number 
# must be 1/3rd of number stored at 4th position.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #List created

print("Sum of last 4 elements:", sum(numbers[-4:])) #Sum of last 4 elements

print("Difference between max and min:", max(numbers)-min(numbers)) #Difference between max and min

numbers.insert(5,numbers[3] / 3) #Insert 1/3rd of the 4th element at the 6th position

print("List after insertion:", numbers) #List after insertion