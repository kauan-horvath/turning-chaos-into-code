"""
############################
# Discovering web scraping
############################

DATE - 2026-04-01

MILESTONES:
- Installing beautifulsoup4 [x]
- Connection stability & error handling [x]
- Target data extraction (H3 > a > Title) [x]
- Implementing a find_all [x] #did in v2

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
    url = "http://books.toscrape.com/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    }

    print(f"Now accessing the url: {url} ")

    try:

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            print("CONNECTED")
            return response.text
        else:
            print(f"FAILED TO CONNECT | STATUS {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        print(
            "TIMEOUT, the website took too long to provide access or rejected this attempt"
        )
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")


def parse_html(content):
    soup = BeautifulSoup(content, "html.parser")

    book_found = soup.find("h3")

    if book_found:
        book_title = book_found.find("a")["title"]
        print(f"That's the book found: {book_title}")
    else:
        print("Book NOT FOUND")


if __name__ == "__main__":
    raw_content = connection()

    if raw_content:
        parse_html(raw_content)
    else:
        print("the website content is empty")
