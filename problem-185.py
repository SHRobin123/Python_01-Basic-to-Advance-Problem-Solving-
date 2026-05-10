#Web Scraper Example

import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.text

print("Website Title:", title)

'''
output:-

Website Title: Example Domain
'''