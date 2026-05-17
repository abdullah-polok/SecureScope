import os

from pyfiglet import figlet_format
from modules.file_integrity import fileIntegrity
from modules.packet_sniffer import packetSniffer
from modules.keylogger import keylogger
from modules.password_analyzer import passwordAnalyzer
from modules.port_scanner import portScanner
from modules.vulner_scanner import vulnerScanner
from modules.web_login_guesser import webLoginGusser
from modules.website_crawler import websiteCrawler
from modules.subdomain_scanner import domainFinder


# # Clear terminal screen
# def clear_screen():
#     os.system("cls" if os.name == "nt" else "clear")


# ASCII Banner
def banner():
   print(figlet_format("SecureScope"))

   print("""
==================================================

        Scan | Monitor | Analyze | Protect

==================================================
        SECURESCOPE - SECURITY TOOLKIT
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
 while True:
    # clear_screen()
     banner()

     choice = input("Select a module: ")

     if choice == "1":
      if __name__ == "__main__":
       fileIntegrity.fileIntegrityChecker.check_integrity()
     elif choice == "2":
        packetSniffer.packetSniffer.start_sniffer()

     elif choice == "3":
        keylogger.keylogger.start_keylogger()
     elif choice == "4":
        password = input("Enter password: ")
        passwordAnalyzer.passwordAnalyzer.analyze_password(password)

     elif choice == "5":
        target = input("Enter target IP/Host: ")
        portScanner.portScanner.scan_ports(target)

     elif choice == "6":
        target = input("Enter target IP/Host: ")
        vulnerScanner.vulnerScanner.scan_vulnerabilities(target)

     elif choice == "7":
        url = input("Enter login URL: ")
        webLoginGusser.webLoginGusser.guess_logins(url)

     elif choice == "8":
        url = input("Enter website URL: ")
        websiteCrawler.websiteCrawler.crawl_website(url)

     elif choice == "9":
        domain = input("Enter domain: ")
        domainFinder.domainFinder.find_subdomains(domain)

     elif choice == "0":
        print("Exiting SecureScope...")
        break

     else:
        print("Invalid option!")

     input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()