import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def scrape(my_url, input1, input2):
    #url input
    URL = my_url
    #make it so that chrome doesnt open up and so that header user agent allows the scraper through
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"+"AppleWebKit/537.36 (KHTML, like Gecko)"+"Chrome/87.0.4280.141 Safari/537.36")

    # Page content from Website URL
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(URL)

    # parse html content
    pageSource = driver.page_source
    bs = BeautifulSoup(pageSource, "lxml")
    bs1 = BeautifulSoup(pageSource, "lxml")

    # user inputs two texts and then we recompile them according to whats on the webpage in case the user input is incomplete
    #user input can be incomplete but it cannot be mispelled
    user_input1 = input1
    user_input2 = input2
    pattern1 = re.compile(user_input1)
    pattern2 = re.compile(user_input2)

    #method to find what type of tag user input text is
    def find_tag_element(pattern):
        # Anchor tag
        a_tag = bs.find('a', text = pattern)
        if a_tag:
            return "a"
        # Span tag
        span_tag = bs.find('span', text = pattern) 
        if span_tag:
            return "span"
        # Heading tag
        h2_tag = bs.find('h2', text = pattern) 
        if h2_tag:
            return "h2"
        h3_tag = bs.find('h3', text = pattern) 
        if h3_tag:
            return "h3"
        h4_tag = bs.find('h4', text = pattern) 
        if h4_tag:
            return "h1"
        # List tag
        li_tag = bs.find('li', text = pattern) 
        if li_tag:
            return "li"
        ul_tag = bs.find('ul', text = pattern) 
        if ul_tag:
            return "ul"
        ol_tag = bs.find('ol', text = pattern) 
        if ol_tag:
            return "ol"
        # div 
        div_tag = bs.find('div', text = pattern)
        if div_tag:
            return "div"
        # p
        p_tag = bs.find('p', text = pattern)
        if p_tag:
            return "p"
        else:
            return "Tag not found"

    #input our text into the methos
    element_tag = find_tag_element(pattern1)

    #use beautiful soup to find the element on the page
    text1 = bs.find(element_tag, text = pattern1)
    text2 = bs.find(element_tag, text = pattern2)

    #get all the parent elements
    # we will only really use the first one, but we need to clear the element itself from it
    parents1 = []
    for parent in text1.parents:
        parents1.append(parent)
        parent.clear()

    #where the results will be stored
    final_items = []

    #find if they have a class name
    if text1.has_attr("class") and text2.has_attr("class"):
        #if they have a class name is it the same for both
        if (text1['class'] == text2['class']):
            #convert the class name to string because some websites its returned as a list if the class name is composed of various elements
            convert_string = ' '.join([str(item) for item in text1['class']])
            #find all other elements with same class name
            find_by_class = bs1.find_all(element_tag, class_=text1['class'])
            #iterate through all the elements and evaluate their attributes and parent/parent attributes to filter out further
            for item in find_by_class:
                if item.attrs.keys() == text1.attrs.keys():
                    if item.parent.name == parents1[0].name:
                        if item.parent.attrs.keys() == parents1[0].attrs.keys():
                            final_items.append(item)
                            print(item)
                            print()
    #if no class name
    #find related items based on the element tag instead of class name
    else:
        related_items = bs1.find_all(element_tag)
        #iterate through all the elements and evaluate their attributes and parent/parent attributes to filter out further
        for item in related_items:
            if item.attrs.keys() == text1.attrs.keys():
                if item.parent.name == parents1[0].name:
                    if item.parent.attrs.keys() == parents1[0].attrs.keys():
                        final_items.append(item)
                        print(item)
                        print()

    #finally close the driver
    driver.close()
