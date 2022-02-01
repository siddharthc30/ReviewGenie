from bs4 import BeautifulSoup
import re

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
x = soup.find("div")
y = x.find_all("span")

p = re.compile(r'<.*?>')
final_text = p.sub('0', str(y))
print(final_text)
