from bs4 import BeautifulSoup
import requests

class scrap():
    
    def file_scrap(self):
        file_name = input("enter the file name which you need to access: ")
        with open (file_name, "r") as f:
            doc = BeautifulSoup(f, "html.parser")
        print(doc.prettify())
    
    def web_scrap():
        link = input("enter the website link which you needed to access: ")
        result = requests.get(link)
        doc = BeautifulSoup(result.text, "html.parser")
        print(doc.prettify())
