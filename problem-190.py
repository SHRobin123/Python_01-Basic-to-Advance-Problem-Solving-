#URL Shortener Example

import random
import string

# dictionary database
url_database = {}

def generate_short_code():

    characters = string.ascii_letters + string.digits

    short_code = ''.join(random.choice(characters) for i in range(6))

    return short_code

def shorten_url(long_url):

    short_code = generate_short_code()

    url_database[short_code] = long_url

    return short_code

def get_original_url(short_code):

    return url_database.get(short_code, "URL not found")

# input long URL
long_url = input("Enter long URL: ")

# generate short URL
short_url = shorten_url(long_url)

print("Short URL:", short_url)

# retrieve original URL
print("Original URL:", get_original_url(short_url))

'''
output:-

Enter long URL: https://www.google.com/search/python

Short URL: A7xK9p

Original URL: https://www.google.com/search/python
'''