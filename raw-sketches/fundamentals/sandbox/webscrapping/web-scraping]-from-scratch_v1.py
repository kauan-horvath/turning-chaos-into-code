
import requests
from bs4 import BeautifulSoup
    #forgot the name is beautifulsoup kk

def connection():
    #definig the url:
    url = "http://books.toscrape.com/"

    #defining the user_agent:
    header = {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    } #grabbed from the browser! and forgot the syntax of dicts "key":"value" forgot the aspas of the key

    print(f"Now acessing the url: {url} ")

    try:
        
        response = requests.get(url, headers=header, timeout=10)
            #creating a var reponse
            #asking to the request ibrary to "get"
            #the url, with the user agent and with a timeout
        
        if response.status_code == 200:
            #checking with .status_code if its 200 or connected
            print("CONNECTED")
            return response.text
            #not sure why return response as text (cheking after)
        else:
            print(f"FAILED TO CONNECT | STATUS {response.status_code}")
            return None
            #making sure of being able to identify what to debug

    #research this except syntaxes
    except requests.exceptions.Timeout:
        print("Timeout, the website took too long to provide acess or rejected this attempt")
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")
        #also making sure to debug 

        #now the connections is established and pulled a lot of txt i have to desegment and work with

def parse_html(content):
    #developing the translator or parser for the raw_content
    soup = BeautifulSoup(content, "html.parser")
        #soup is the func deposit
        #the library requires: content with the content
        # "html-parser" is the language of translation for the bs4

    #storaging the first book found (all info)
    books_found = soup.find("h3")

    if books_found:
        #retrieving just the title from the raw:
        """ How is in the website:
        <a href="link.html" title="A Light in the Attic" class="link-book">
        so find the tag <a and grab the value in [title]
        """    
        book_title = books_found.find("a")["title"]
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