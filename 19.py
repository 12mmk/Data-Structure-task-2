# . Initialize a list emails and initialize a set blacklisted emails.
# Set current_email = ‘hari77@test.com’.
# Write a program that checks if current_email is in all_emails but not in
# blacklisted. Print "Email Sent" if safe, or "Blocked" if it fails either condition.

emails = ['ram123@gmail.com','hari77@gmail.com']
blacklisted_emails = {'hari77@gmail.com'}

current_email = 'hari77@gmail.com'

if current_email in emails and not(current_email in blacklisted_emails):
    print("Email Sent")
else:
    print("Blocked")

