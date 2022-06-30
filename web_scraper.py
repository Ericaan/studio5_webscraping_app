from tokenize import String
from tracemalloc import stop
from unittest import result
from bs4 import BeautifulSoup
import requests

#1 is for the first element selected and 1a for the second element selected

URL = 'https://www.geeksforgeeks.org/'

# Page content from Website URL
page = requests.get( URL )

# parse html content
soup = BeautifulSoup( page.content , 'lxml')
soup1 = BeautifulSoup( page.content , 'lxml')

# define a pattern(certain text)
pattern = 'Oracle Netsuite Interview Experience (On-Campus)'

#method to find what type of tag user input text is
def find_tag_element(pattern):
    # Anchor tag
    a_tag = soup.find_all('a', text = pattern)
    if a_tag is not None:
        return "a"
    # Span tag
    span_tag = soup.find_all('span', text = pattern) 
    if span_tag is not None:
        return "span"
    # Heading tag
    h2_tag = soup.find_all('h2', text = pattern) 
    if h2_tag is not None:
        return "h2"
    h3_tag = soup.find_all('h3', text = pattern) 
    if h3_tag is not None:
        return "h3"
    h4_tag = soup.find_all('h4', text = pattern) 
    if h4_tag is not None:
        return "h1"
    # List tag
    li_tag = soup.find_all('li', text = pattern) 
    if li_tag is not None:
        return "li"
    ul_tag = soup.find_all('ul', text = pattern) 
    if ul_tag is not None:
        return "ul"
    ol_tag = soup.find_all('ol', text = pattern) 
    if ol_tag is not None:
        return "ol"
    # div 
    div_tag = soup.find_all('div', text = pattern)
    if div_tag is not None:
        return "div"
    # p
    p_tag = soup.find_all('p', text = pattern)
    if p_tag is not None:
        return "p"

#input our text into the methos
element_tag = find_tag_element(pattern)

#use beautiful soup to find the element on the page
text1 = soup1.find(element_tag, text = pattern)

#get all the parent elements 
#define list for parents 
parents1 = []
#iterate through the parents, delete the child element(this stops the child from showing up over and over), and add to the list
for parent in text1.parents:
    parents1.append(parent)
    parent.clear()

#list of all the items with same html element tag
related_items = soup.find_all(element_tag)
# where our desired items will be collected
final_items = []

#iterate through the related items and see if they are similar in attributes to out element and its parent's attributes
for item in related_items:
    if item.attrs.keys() == text1.attrs.keys():
        if item.parent.attrs.keys() == parents1[0].attrs.keys():
            final_items.append(item)
            print(item)
            print()

