from bs4 import BeautifulSoup


html_data = '''
<div>
<span class="a-size-base review-text review-text-content" data-hook="review-body">
<span>
  Great product. Excellent performance
</span>
</span>
</div>
'''
soup = BeautifulSoup(html_data, 'html.parser')
x = soup.findAll("div")
y = x.find_all("span")
print(x)