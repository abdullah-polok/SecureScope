"""
This module implements a simple packet sniffer using the Scapy library. 
It captures network packets on a specified interface and displays their contents.

Development steps:
=> Import necessary libraries (Scapy)
=> Define a function to start sniffing on a given interface
=> Define a callback function to process each sniffed packet
=> Get the interface to sniff on from user input

"""

import scapy.all as scapy
import scapy.all as scapy



# Function to start sniffing on a specified interface
def sniffer():

    interface = input("Enter the interface to sniff on (e.g., eth0, wlan0): ")
# Use Scapy's sniff function to capture packets on the specified interface    
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

# Callback function to process each sniffed packet
def process_sniffed_packet(packet):
   # Print the summary of the packet 
    print(packet.show())


