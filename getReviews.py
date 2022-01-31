import requests
from bs4 import BeautifulSoup

query = input("Enter the ASIN code of the amazon product: ")
base_url = "https://www.amazon.in/dp/"
query_url = base_url + query

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

search_response = requests.get(query_url, headers = headers)
response_code = search_response.status_code

content = search_response.text

soup = BeautifulSoup(content, "lxml")

all_reviews = [link['href'] for link in soup.find_all("a", {'data-hook': 'see-all-reviews-link-foot'}, href = True)]

base = "https://www.amazon.in"

reviews_page_url = base+' '.join(all_reviews)

review_page_source = requests.get(reviews_page_url, headers = headers)

final_reviews = []

soup = BeautifulSoup(review_page_source.text, "lxml")
x = soup.find_all("span", {'data-hook' : 'review-body'}, limit = 10)


print(x)

    









