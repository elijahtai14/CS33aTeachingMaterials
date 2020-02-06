# We are making a web scraper
import requests
from bs4 import BeautifulSoup

page = requests.get("https://cs50.harvard.edu/extension/web/2020/spring/")
soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())
