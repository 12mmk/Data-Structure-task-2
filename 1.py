# Create a dictionary mapping student names to email addresses
# write a program that prompts for the user for a name 
# if the name exists display the email 
# otherwise display contact not found. 

student_emails = { 
    '1': {'name': 'ram', 'email': 'ram@gmail.com'},
    '2': {'name': 'shyam', 'email': 'shyam@gmail.com'},
    '3': {'name': 'hari', 'email': 'hari@gmail.com'}
    }             

name = input('Enter the name of the student: ')
id_num = input("Enter the student's ID number: ")
name = name.lower()

if id_num in student_emails:
    print("Email : ",student_emails[id_num]['email'])
else:
    print('Contact not found.')

