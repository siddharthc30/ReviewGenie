from contextlib import nullcontext
from logging import NullHandler
from bs4 import BeautifulSoup
import requests

search_query = "palace heights"
search_query = search_query.split()
search_query = "+".join(search_query)

url = "https://google.com/search?q=" + search_query

content = requests.get(url)
parser = "html.parser"
soup = BeautifulSoup(content.text, parser)

reviews = soup.find('span', {"class" : "Aq14fc"})

print(reviews)
