"""
This module provides a simple port scanner that can be used to check for open ports on a target IP address. 
The user can input the target IP address and a list of ports to scan, and the module will return a list of open ports.

Development Steps
=> Import necessary libraries (socket)
=> Define a function to scan ports
=> Create a socket and try to connect to the target on each specified port
=> Set a timeout for the connection
=> Check the result of each connection attempt and store open ports
=> Close the socket after each try
=> Get user input for target IP address and ports to scan

"""

import socket

def scan_ports(target,ports):
    open_ports=[]
    for port in ports:
  # Create a socket and try to connect to the target on the specified port
        sock=socket.socket( socket.AF_INET, socket.SOCK_STREAM)
  # Set a timeout for the connection
        sock.settimeout(1)
  # Use connect_ex to try the connection and check the result
        result=sock.connect_ex((target,port))
        if result==0:
            open_ports.append(port)
        sock.close()
    return open_ports


input_target=input("Enter the target IP address: ")
input_ports=input("Enter the ports to scan (comma separated): ")
print(scan_ports(input_target, [int(port.strip()) for port in input_ports.split(",")]))