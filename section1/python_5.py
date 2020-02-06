# We are making a web scraper
import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, url):
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, "html.parser")
    
    def returnLinks(self):
        for link in self.soup.find_all('a'):
            print(link.get('href'))

    def printPage(self):
        print(self.soup.prettify())

p = Parser("https://cs50.harvard.edu/extension/web/2020/spring/")
print(p.returnLinks())

p2 = Parser("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
print(p2.returnLinks())
