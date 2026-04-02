"""
##################################
# Second reconstruction by head - Sucess
##################################

DATE - 2026-04-02

MILESTONES:
- Remake the entire basic scrape structure by head [x]
- recollect an User-Agent [x]
- note all mistakes and progress [x]
- implement a find_all [x]

PROGRESS:
    - Discovered the webterminal 
        - i can easily find indo trought browser not only clicking in network but also typing: navigator.user-agent
    - Remembered the .get() syntax perfectly
        - request.get(url, user-agent-dict, timeout=10)
    - Sucessfuly remember the steps of the software
        - imports ✔️
        - connecting ✔️
        - parsing ✔️

FAILURES:
Basic errors - completely avoidable mistakes
    - Never try to rewrite the url [copy and paste for safety]
    - Forgot to UPPERcase the missing User-agent 
        started the program without replacing the missing data
    - Discovered that .status_code is without () 
        which lead me to .text also without () [Method vs Atribute]
    - Forgot that the right name is "html.parser" with a dot.
Intermediate errors - memory failures 
    - completely forgot the syntax of the excepts
        - except library.value
            - except requests.timeout:
        - except library.exceptions.value
            - except requests.exceptions.requestexception
            (capture any kind of error with requests)
advanced missings - after research what's missing
    - apply diferent request trought the html
    - apply a find_all() syntax after this on setle down
    - elevate the level of web scraping
"""

####################################
import os
import time
import requests
from bs4 import BeautifulSoup

def connecting():
    url = "http://books.toscrape.com/"

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    }

    print(f"Atempting connection to: {url}")
    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            print("CONNECTED")
            return response.text 
        
        else:
            print(f"Failed to connect | Status: {response.status_code} ")
            return None
        
    except requests.Timeout:
        print("TIMEOUT")
    except requests.exceptions.RequestException as e:
        print(f"critial error | {e}")

# def parse_html(content):
#     soup = BeautifulSoup(content, "html.parser") 

#     book_found = soup.find("h3")

#     if book_found:
#         book_title = book_found.find("a")["title"]
#         print(f"The book found is: {book_title}")

#     else:
#         print("Book Not found")

def parse_html(content):
    soup = BeautifulSoup(content, "html.parser") 

    all_books = soup.find_all("h3")
    print("-" * 30)
    for book in all_books:
        book_title = book.find("a")["title"]
        print(f"📗: {book_title}")
        time.sleep(0.5)

    else:
        print("Book Not found")

if __name__ == "__main__":
    raw_content = connecting()

    if raw_content:
        os.system("cls" if os.name == "nt" else "clear")
        parse_html(raw_content)