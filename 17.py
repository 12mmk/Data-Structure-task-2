# 17. Initialize a dictionary
# Write a program that checks if the score is greater than or equal to 80. If it
# is, add a new key status to the dictionary with the value Pass. If not, set
# status to Review. Print the final dictionary.


student_data = {'name':'Sam','score':85}
if student_data['score']>=80:
    student_data['status'] = 'Pass'
else:
    student_data['status'] = "Review"
print(student_data)