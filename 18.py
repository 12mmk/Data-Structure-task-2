# Define a dictionary

database = {'admin':'1234', 'user':'abcd'}

#Define two variables 
user_inputs = 'admin'
user_pass = '1234'

if user_inputs in database:
    if user_pass==database[user]:
        print("Login Successful")
    else:
        print("Login Unsuccessful")
else:
    print("User does not exists")
