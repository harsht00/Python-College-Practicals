#Create dictionary
students = {
   101: {"Name": "Shreepad", "Scores": [10,20,25]},
   102: {"Name": "Swaraj", "Scores": [45,60,50]},
   103: {"Name": "Harsh", "Scores": [80,70,90]},
   104: {"Name": "Pravin", "Scores": [45,60,70]},
   105: {"Name": "Om", "Scores": [85,90,80]}
}

#calculate average score and flag pass fail
for sid, details in students.items():
    avg = sum(details["Scores"]) / len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >= 50 

 #print students who passed
print("Students who passed:")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"]) 
