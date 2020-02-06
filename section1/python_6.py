# We are making a web scraper
import requests
from bs4 import BeautifulSoup

def statusDecorator(f):
    def wrapper(*args):
        print("Working on: " + args[0].url)
        res = f(args[0])
        print("Done working on: " + args[0].url)
        return res
    return wrapper

class Parser:
    def __init__(self, url):
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, "html.parser")
        self.url = url

    @statusDecorator
    def returnLinks(self):
        links = []
        for link in self.soup.find_all('a'):
            links.append(link.get('href'))
        return links

    def printPage(self):
        print(self.soup.prettify())

p = Parser("https://cs50.harvard.edu/extension/web/2020/spring/")
print(p.returnLinks())