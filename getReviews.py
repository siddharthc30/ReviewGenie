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
    all_reviews = [link for link in soup.find_all("a", {'data-hook': 'see-all-reviews-link-foot'}, href = True)]
    reviews_page_url = base+' '.join(all_reviews)
    print(reviews_page_url)
    #get request to all reviews page
    review_page_source = requests.get(reviews_page_url, headers = headers)
    final_reviews = []

    # parsing and storing the reviews
    soup = BeautifulSoup(review_page_source.text, "html.parser")
    for i in soup.findAll("span", {'data-hook' : 'review-body'}, limit = 10):
        #for k in i.find_all("span"):
        final_reviews.append(i.get_text().strip())
    
    return final_reviews



def process_reviews(final_reviews):
    '''
    Function to preprocess the scraped reviews(emojies if any)

    Arguments:
    Array with each element as a review

    Returns:
    Processed array without any emojies
    '''
    processed_reviews = []
    emoji_pattern = re.compile(
    "(["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "])"
  )
    for r in final_reviews:
        processed_reviews.append(emoji_pattern.sub('', r))

    return processed_reviews






