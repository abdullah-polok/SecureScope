"""
This module is used to evaluate password strength and 
Checks whether passwords is strong or weak based one Regex 
and helps users create stronger and more secure passwords


Develooment steps:

=> Take password input
=> Check password length
=> Verify uppercase/lowercase letters
=> Check numbers and special characters
=> Analyze password complexity
=> Display strength result

"""
import re


def password_strength():
    password = input("Enter your password: ")
    if len(password)<8:
        print("Password should be at least 8 characters")
    elif not re.search("[a-z]",password):
        print("Password should contain at least one lowercase letter:")
    elif not re.search("[A-Z]",password):
        print("Password should contain at least one uppercase letter:")
    elif not re.search("[0-9]",password):
        print("Password should contain at least one number:")
    elif not re.search("[!@#$%^&*(),.?\":{}|<>]",password):
        print("Password should contain at least one special character:")
    else:
        print("Password is strong")
    




