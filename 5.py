grades = {"ram": 92, "sita": 88}
# write  a program to check if a specific students name exissts as key, 
# if found  print their grade otherwise indicate that the grade is not available.

student_name = input("Enter the student's name: ")
student_name = student_name.lower()
if student_name in grades:
    print(f"{student_name}'s grade is: {grades[student_name]}")
else:
    print("Grade not available.")