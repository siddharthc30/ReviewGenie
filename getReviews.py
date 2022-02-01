import requests
from bs4 import BeautifulSoup
import re

def getreviews(query):
    '''
    Function to extract top 10 reviews of a product on amazon.in

    Arguments:
    ASIN code of the product in string

    Returns:
    An array with raw reviews(contains html tags)
    '''

    base = "https://www.amazon.in"
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    query_url =  base + "/dp/" + query
    #s = requests.Session()

    # get request to main product page
    search_response = requests.get(query_url, headers = headers)
    content = search_response.text
    soup = BeautifulSoup(content, "html.parser")

    #finding the link to all reviews page
    all_reviews = [link['href'] for link in soup.find_all("a", {'data-hook': 'see-all-reviews-link-foot'}, href = True)]
    reviews_page_url = base+' '.join(all_reviews)

    #get request to all reviews page
    review_page_source = requests.get(reviews_page_url, headers = headers)
    final_reviews = []

    # parsing and storing the reviews
    soup = BeautifulSoup(review_page_source.text, "html.parser")
    for i in soup.findAll("span", {'data-hook' : 'review-body'}, limit = 10):
        #for k in i.find_all("span"):
        final_reviews.append(i)
    
    return final_reviews



def process_reviews(final_reviews):
    '''
    Function to preprocess the scraped reviews(removes html tags, empty spaces and emojies if any)

    Arguments:
    Array with each element as a review

    Returns:
    Processed array without any junk
    '''
    processed_reviews = []
    p = re.compile(r'<.*?>')
    for r in final_reviews:
        processed_reviews.append(p.sub('', r))

    return processed_reviews

arr = getreviews("B09G9HR5GX")
print(arr)
print(process_reviews(arr))





