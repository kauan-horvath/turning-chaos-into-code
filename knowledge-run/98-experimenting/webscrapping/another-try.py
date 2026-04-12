"""
####################
# Just a Run for quick practice
####################

DATE - 2026-04-04

MILESTONES:
- Remake from scratch [x]
- Check my deep understanding [x]
- check syntax and ortography [x]

FUTURELY:
develop a way to check prices and other classes[]

PROGRESS:
Bs4 Soup - sucessfully remembered the library features
Structure - Quickly structured the base of the scraping


FAILURES:
Missing data inside of try - Forgot that the response should be inside the try
Except Syntax - Forgot how to correctly recall request.exceptions
"""

####################################
import requests
from bs4 import BeautifulSoup


# FUNCTIONS


def conection():

    URL = "http://books.toscrape.com/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    }

    try:
        web_response = requests.get(URL, headers=headers, timeout=10)

        if web_response.status_code == 200:
            print(f"CONECTED TO: {URL}")
            return web_response.text
        else:
            print(f"Failed to conect | Status {web_response.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("The server took too long to respond")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Critical Error: {e}")
        return None


def parser_html(content):
    soup = BeautifulSoup(content, "html.parser")

    books_data = soup.find_all("h3")

    for book in books_data:
        book_title = book.find("a")["title"]
        print(f"📗: {book_title}")


# MAIN LOOP

if __name__ == "__main__":
    raw_content = conection()
    if raw_content:
        parser_html(raw_content)
    else:
        print("empty html")
