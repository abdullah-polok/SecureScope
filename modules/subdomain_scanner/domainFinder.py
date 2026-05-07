'''
Sub domain Scanner(enumeration)
This module is used to find subdomains of a given domain. It uses a wordlists to find subdomains of that website.

'''

import dns.resolver

resolver=dns.resolver.Resolver()
subdomains=["wwww","mail","webmail","ftp","api","mail","server","dev","moodle"]




#function to find subdomains
def subdomain_finder(domain):
    for subdomain in subdomains:


        #error handling using try and except to handle the errors 
        #the code will try to resolve the subdomain and if it finds it, it will print it. If it doesn't find it, it will pass and move on to the next subdomain in the list.
        try:
            full_domain=subdomain+"."+domain
            #
            answers=resolver.resolve(full_domain) #the resolver will try to resolve the full domain name and if it finds it, it will print it. If it doesn't find it, it will raise an exception and the code will move on to the next subdomain in the list.
            print(f"Subdomain found: {full_domain}")
            
        except dns.resolver.NoAnswer:
            print(f"No answer for: {full_domain}")



# function call using the domain name as an argument
subdomain_finder("ukh.edu.krd") 





        