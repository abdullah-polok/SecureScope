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


def password_strength(password):
    if len(password)<8:
        return "Password should be at least 8n characters"
    elif not re.search("[a-z]",password):
        return "Password should contain at least one lowercase letter:"
    elif not re.search("[A-Z]",password):
        return "Password should contain at least one uppercase letter:"
    elif not re.search("[0-9]",password):
        return "Password should contain at least one number:"
    elif not re.search("[!@#$%^&*(),.?\":{}|<>]",password):
        return "Password should contain at least one special character:"
    else:
        return "Password is strong"
    


input_password = input("Enter your password: ")
result = password_strength(input_password)
print(result)