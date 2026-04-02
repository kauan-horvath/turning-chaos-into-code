"""
############################
# Discovering web scraping
############################

DATE - 2026-04-01

MILESTONES:
- Installing beautifulsoup4 [x]
- Connection stability & error handling [x]
- Target data extraction (H3 > a > Title) [x]
- Implementing a find_all [ ]

PROGRESS:

    - Learned the classical syntax for a chrome User-Agent:
        - find where to find or what to google to obtain

        Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
        
    - Learned the scraping structure:
        Request > User-Agent >
        Response > status200
        Parser > Bs4 receive raw_html and create the soup
        Extraction > navigate through h3 -> a -> title

FAILURES:
    - CLASSICAL ERROR 404 - short mistake on the url created a not found return on the scraping 
        "https://remote.co/remote-jobs/design": instead of safely copying the url i decide to write down and made a few spelling errors like remote.com and designs instead of remote.co or design in singular

    - CLASSICAL TIMEOUT - forgot to implement a timeout break to avoid the coding running for ever
        by fixing this discovered the syntax of get(timeout=)

    - ACCESS DENIED - remote.co locked my request, so i've changed for a friendly website for studying scrape: 
        "http://books.toscrape.com/"

"""

import requests
from bs4 import BeautifulSoup

def connection():
    #defining the url:
    url = "http://books.toscrape.com/"

    #defining the User-Agent:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    } #grabbed from the browser! and forgot the syntax of dicts "key":"value" forgot the quotation marks of the key

    print(f"Now accessing the url: {url} ")

    try:
        
        response = requests.get(url, headers=headers, timeout=10)
            #creating a var reponse
            #asking to the request ibrary to "get"
            #the url, with the User-Agent and with a timeout
        
        if response.status_code == 200:
            #checking with .status_code if its 200 or connected
            print("CONNECTED")
            return response.text
            #converting into full string to not break the parse
        else:
            print(f"FAILED TO CONNECT | STATUS {response.status_code}")
            return None
            #making sure of being able to identify what to debug
                #response.content > used by pdfs
                #response.json > access api return dict 

    #research this except syntaxes
    except requests.exceptions.Timeout:
        print("TIMEOUT, the website took too long to provide access or rejected this attempt")
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")
        #also making sure to debug 

        #now that the connection is established and pulled a lot of txt i have to desegment and work with on parse

def parse_html(content):
    #developing the translator or parser for the raw_content
    soup = BeautifulSoup(content, "html.parser")
        #soup is the func deposit
        #the library requires: content with the content
        # "html-parser" is the language of translation for the bs4

    #storaging the first book found (all info)
    book_found = soup.find("h3")

    if book_found:
        #retrieving just the title from the raw:
        """ How is in the website:
        <a href="link.html" title="A Light in the Attic" class="link-book">
        so find the tag <a and grab the value in [title]
        """    
        book_title = book_found.find("a")["title"]
        print(f"That's the book found: {book_title}")
    else:
        print(f"Book NOT FOUND")

    pass


if __name__ == "__main__":
    #depositing the full html of the website
    raw_content = connection()

    if raw_content:
        parse_html(raw_content)
    else:
        print("the website content is empty")