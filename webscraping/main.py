from importlib.resources import contents
from bs4 import BeautifulSoup

with open ('G:\Praktek_Coding\Web_Scraping\webscraping\home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h2')
    print(tags) 