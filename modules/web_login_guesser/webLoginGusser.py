"""
This module is used to test login forms with multiple username and password combinations.
Demonstrates risks of weak passwords and poor authentication security and
Commonly used in penetration testing and security auditing

Development Steps

=> Identify target login page
=> Analyze login request parameters
=> Load username or password wordlist
=> Send automated login attempts
=> Detect successful or failed responses
=> Store and display results
"""

import requests

def web_login_gusser():
    url = input("Enter the login URL: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
# This function try to log in to a web application using the provided URL, username, and password  
    try:
        #send a post request to the login website with the given username and password
        response = requests.post(url, data={'username': username, 'password': password})
   
      # check the reponse statud code and print the result of the login username and password 
        if response.status_code == 200:
            print(f"Login successful for {username}:{password}")
        else:
            print(f"Login failed for {username}:{password}")
    except Exception as e:
        print(f"An error occurred: {e}")
