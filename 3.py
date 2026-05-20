# starting with write a program to add a new student. 
# the student should onl y be added if they are not already int the list. 
# print a confirmatoion or an laready present message.
class_list = ['ram', 'sita', 'laxman']

new_student = input('Enter the name of the new student: ')
new_student = new_student.lower()

if new_student in class_list:
    print(f"{new_student} is already in the class list.")   
else:
    class_list.append(new_student)
    print(f"{new_student} has been added to the class list.")

