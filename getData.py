import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('/home/siddharthc30/Documents/chromedriver', chrome_options = options)

def getdata(query):
    '''
    Function to extract top 10 reviews of a product on amazon.in

    Arguments:
    ASIN code of the product in string

    Returns:
    An array with raw reviews(contains html tags)
    '''
    #dictionary to store image url, rating and reviews
    data = {}

    base = "https://www.amazon.in"
    query_url =  base + "/dp/" + query

    driver.get(query_url)

    content_for_image = driver.page_source
    soup = BeautifulSoup(content_for_image, "html.parser")

    #getting image url
    image_tag = soup.find("img", {'data-a-image-name':'landingImage'})
    image_url = image_tag.get('src')
    data['Image'] = image_url

    # navigating to all reviews page
    button = driver.find_element_by_css_selector("a[data-hook = 'see-all-reviews-link-foot']")
    button.click()

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    #getting overal product rating
    rating_tag = soup.find("span", {'data-hook':'rating-out-of-text'})
    rating_text = rating_tag.get_text()
    product_rating = rating_text
    data['Rating'] = product_rating


    #getting user reviews
    final_reviews = []

    # parsing and storing the reviews
    for i in soup.findAll("span", {'data-hook' : 'review-body'}, limit = 10):
        #for k in i.find_all("span"):
        final_reviews.append(i.get_text().strip())
    
    data['Reviews'] = final_reviews
    
    return data



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

if __name__ =="__main__":
    print(getdata("B01J1CFO5I"))





