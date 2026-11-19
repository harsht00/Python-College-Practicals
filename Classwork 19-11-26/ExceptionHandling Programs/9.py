#Printing report
try:
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100")

    if marks >= 75:
        grade = "A"

    elif marks >= 60:
        grade = "B"

    elif marks >= 40:
        grade = "C"

    else:
        grade = "F"

except ValueError as e:
    print("Error:", e)

else:
    print("\nStudent Report")
    print("--------------------")
    print("Roll No :", roll)
    print("Name    :", name)
    print("Marks   :", marks)
    print("Grade   :", grade)
