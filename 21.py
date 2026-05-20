#  You are developing a student enrollment module. The system must verify
# course availability and student eligibility using different Python collection
# types to ensure data integrity. Write a Python script that implements an
# enrollment gatekeeper using the following requirements.
# Create a set called valid_courses containing python, robotics, java and create
# a list called hs_grades containing integers 9 through 12.
# Capture and Store Data, use input() to collect a student's name, course, and
# grade as an integer. Store these three values inside a single Dictionary
# named student_records. Use if-else statements to evaluate the data in this
# exact order:

# 1. Check if the requested course exists in the valid_courses set. If not, print:
# {name} selected an invalid course.

# 2. If the course is valid, check if the student's grade is within the hs_grades
# list. If the grade is less than 9, print grade too low and if greater than 12,
# # print grade too high.

# 3. If they pass both checks, apply the robotics rule, if the course is robotics
# and the grade is 9, they are ineligible.
# If they pass, print {name} is approved for {course}
# If they fail, print {name} is not eligible for {course} grade too low

valid_courses = set()
valid_courses = ("python", "robotics","java")
hs_grades = [9,10,11,12]

student_name = input("Enter student's name : ")
course = input("Enter student's course : ")
grade = int(input("Enter your grade : "))

student_records = {}
student_records['name'] = student_name
student_records['course'] = course
student_records['grade'] = grade

if course in valid_courses:
    if grade<9:
        print("Grade too low")
    
    elif grade>12:
        print("Grade too high")
    
    elif grade in hs_grades:
        if course == 'robotics' and grade==9:
            print("You are ineligible")
        else:
            print("You are eligible")
            print(f'{student_name} is approved for {course}.')
        

else:
    print(f'{name} selected an invalid course')


