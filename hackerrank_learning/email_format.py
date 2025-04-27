import re

# email_reg = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_reg = r"^[a-zA-Z0-9.]+@[a-zA-Z.]+\.[a-z]$"

input_email_form = input("Nhap email: ")

while(re.search(email_reg, input_email_form) == None):
    input_email_form = input("Nhap email: ")

print("Email valid👌")