import os

from pyfiglet import figlet_format
from colorama import Fore, Style, init


from modules.file_integrity.fileIntegrity import check_integrity
from modules.packet_sniffer.packetSniffer import sniffer
from modules.keylogger.keylogger import start_keylogger
from modules.password_analyzer.passwordAnalyzer import password_strength
from modules.port_scanner.portScanner import scan_ports
from modules.vulner_scanner.vulnerScanner import scan_vulnerabilities
from modules.web_login_guesser.webLoginGusser import web_login_gusser
from modules.website_crawler.websiteCrawler import crawl_website
from modules.subdomain_scanner.domainFinder import subdomain_finder


# # Clear terminal screen
# def clear_screen():
#     os.system("cls" if os.name == "nt" else "clear")


# ASCII Banner
def banner():
   init(autoreset=True)
   print(Fore.CYAN + figlet_format("SecureScope", font="slant"))

   print(Fore.GREEN +"""
==================================================

        Scan | Monitor | Analyze | Protect

==================================================
      Security Toolkit - Abdullah Al Rahman
==================================================

   [1] File Integrity Checker
   [2] Packet Sniffer
   [3] Keylogger
   [4] Password Analyzer
   [5] Port Scanner
   [6] Vulnerability Scanner
   [7] Web Login Guesser
   [8] Website Crawler
   [9] Subdomain Scanner
   [0] Exit

==================================================
""")


# Main program
def main():
 print("Welcome to SecureScope - Your Ultimate Security Toolkit!")
 while True:
    # clear_screen()
     banner()

     choice = input("Select a module: ")

     if choice == "1":
       check_integrity()
     
     elif choice == "2":
        sniffer()

     elif choice == "3":
       start_keylogger()
     
     elif choice == "4":
      password_strength() 
     
     elif choice == "5":
       scan_ports()

     elif choice == "6":
        scan_vulnerabilities()

     elif choice == "7":
        web_login_gusser()

     elif choice == "8":
       crawl_website()

     elif choice == "9":
        subdomain_finder()

     elif choice == "0":
        print("Exiting SecureScope...")
        break

     else:
        print("Invalid option!")
     
     input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()