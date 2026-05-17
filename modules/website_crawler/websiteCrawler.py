
'''
Website Crawler(find links and pages)
This module automatically explores a website extracts and collects links/pages from the target website used for reconnaissance and website mapping

How to develop a website crawler:

=> Take website URL as input
=> Send HTTP request to target page
=> Parse HTML content
=> Extract links (href)
=> Store discovered URLs
=> Avoid duplicate links
=> Continue crawling discovered pages

'''




import requests
from bs4 import BeautifulSoup

def crawl_website():
    # A set to keep track of visited URLs
    visited = set()

    # Get the URL to crawl from the user
    url = input("Enter the URL to crawl: ")

    # make a get request from the website using requests library
    response = requests.get(url)

    # parse html content using BeautifulSoup library

    soup = BeautifulSoup(response.content,"html.parser")

    # find all anchor tags and extract the href attribute
    #https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all
    for link in soup.find_all("a"):
    # extract the href attribute from the anchor tag
      href = link.get("href")


# check if the href is not None and has not been visited before
    if href and href not in visited:
        # add the href to the visited set
        visited.add(href)
        print(href)


