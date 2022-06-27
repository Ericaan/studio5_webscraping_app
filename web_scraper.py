from bs4 import BeautifulSoup
import requests


URL1 = 'https://www.geeksforgeeks.org/'
URL1a = 'https://www.geeksforgeeks.org/'

# Page content from Website URL
page1 = requests.get( URL1 )
page1a = requests.get( URL1a )
# parse html content
soup1 = BeautifulSoup( page1.content , 'lxml')
soup1a = BeautifulSoup( page1a.content , 'lxml')

# define a pattern(certain text)
pattern1 = 'How Learning To Code Can Change Your Life?'
#define a second pattern of the same set of data you want
pattern2 = 'Simplify Your Hiring Process with GFG “Get Hired” Job Portal'

'''
# Anchor tag
text1 = soup.find_all('a', text = pattern)
#print(text1)
# Span tag
text2 = soup.find_all('span', text = pattern) 
#print(text2)
# Heading tag
text3 = soup.find_all('h1', text = pattern) 
#print(text3)
# List tag
text4 = soup.find_all('li', text = pattern) 
#print(text4)
'''

#find the html element and attributes of the pattern
text1 = soup1.find('a', text = pattern1)
text2 = soup1a.find('a', text = pattern2)

#get all the parent elements of both patterns
#define list for parent of first 
parents1 = []
#iterate through the parents, delete the child element(this stops the child from showing up over and over), and add to the list
for parent in text1.parents:
    parent.clear()
    parents1.append(parent)
#same for the second
parents2 = []
#iterate through the parents, delete the child element(this stops the child from showing up over and over), and add to the list
for parent in text2.parents:
    parent.clear()
    parents2.append(parent)


#new list with all the common elements
p1_as_set = set(parents1)
intersection = p1_as_set.intersection(parents2)
common_parents = list(intersection)

print(common_parents)

