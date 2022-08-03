from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import json


#main web scraping function
def scrape(my_url, input1, input2, pages, get_data):
    #url input
    URL = my_url
    #make it so that chrome doesnt open up and so that header user agent allows the scraper through
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)'+'AppleWebKit/537.36 (KHTML, like Gecko)'+'Chrome/87.0.4280.141 Safari/537.36')

    # Page content from Website URL
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(URL)

    # user inputs two texts 
    user_input1 = f'"{input1}"'
    user_input2 = f'"{input2}"'
    #search the page to find the elements that contain the inputs
    text1 = driver.find_element(By.XPATH,f"// *[contains(text(),{user_input1})]")
    text2 = driver.find_element(By.XPATH,f"// *[contains(text(),{user_input2})]")

    #now find all the attributes and such of the elements
    attrs1 = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', text1)
    attrs2 = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', text2)
    t1_class = text1.get_attribute('class')
    t2_class = text2.get_attribute('class')
    t1_tagname = text1.tag_name

    #find the parents and their attributes
    parent1 = driver.execute_script("return arguments[0].parentNode;",text1)
    parent2 = driver.execute_script("return arguments[0].parentNode;",text2)
    p_attrs1 = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', parent1)
    p_attrs2 = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', parent2)
    p1_tagname = parent1.tag_name
    p2_tagname = parent2.tag_name

    #declare a list that will hold the results
    final_items = []

    #function to find and filter all the related elements
    def scrape_url(a_url):
        #start a new webdriver for when there is multiple page results
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(a_url)
        #find if they have a class name
        if t1_class and t2_class:
            #if they have a class name is it the same for both
            if (t1_class == t2_class):
                find_by_class = driver.find_elements(By.XPATH, f"// *[contains(@class,'{t1_class}')]")
                #iterate through all the elements and evaluate their attributes and parent/parent attributes to filter out further
                for item in find_by_class:
                    #do they have the same attributes
                    attrs = {}
                    attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
                    if attrs.keys() == attrs1.keys():
                        #do their parents have the same tag
                        parent = driver.execute_script("return arguments[0].parentNode;",item)
                        if  p1_tagname == parent.tag_name:
                            #do their parents have the same attributes
                            p_attrs = {}
                            p_attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', parent)
                            if p_attrs.keys() == p_attrs1.keys():
                                #add to the list
                                final_items.append(item.get_attribute("innerHTML"))
                                print(item.get_attribute("innerHTML"))
                                print()
                    # in case the item should be added but for some reason differs on one or two attributes
                    elif attrs1.keys() != attrs2.keys():
                        parent = driver.execute_script("return arguments[0].parentNode;",item)
                        if p2_tagname == parent.tag_name:
                            p_attrs = {}
                            p_attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', parent)
                            if p_attrs.keys() == p_attrs2.keys():
                                final_items.append(item.get_attribute("innerHTML"))
                                print(item.get_attribute("innerHTML"))
                                print()
            else:
                #if they dont have a class
                related_items = driver.find_elements(By.TAG_NAME,t1_tagname)
                #iterate through all the elements and evaluate their attributes and parent/parent attributes to filter out further
                for item in related_items:
                    attrs = {}
                    attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
                    if attrs.keys() == attrs1.keys():
                        parent = driver.execute_script("return arguments[0].parentNode;",item)
                        if p1_tagname == parent.tag_name:
                            p_attrs = {}
                            p_attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', parent)
                            if p_attrs.keys() == p_attrs1.keys():
                                final_items.append(item.get_attribute("innerHTML"))
                                print(item.get_attribute("innerHTML"))
                                print()
                    # in case the item should be added but for some reason differs on one or two attributes
                    # make note in instructions if the user isnt getting some desired result add it to one of the inputs
                    elif attrs1.keys() != attrs2.keys():
                        parent = driver.execute_script("return arguments[0].parentNode;",item)
                        if p2_tagname == parent.tag_name:
                            p_attrs = {}
                            p_attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', parent)
                            if p_attrs.keys() == p_attrs1.keys():
                                final_items.append(item.get_attribute("innerHTML"))
                                print(item.get_attribute("innerHTML"))
                                print()
        #if no class name
        #find related items based on the element tag instead of class name
        else:
            related_items = driver.find_elements(By.TAG_NAME,t1_tagname)
            #iterate through all the elements and evaluate their attributes and parent/parent attributes to filter out further
            for item in related_items:
                attrs = {}
                attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
                if attrs.keys() == attrs1.keys():
                    parent = driver.execute_script("return arguments[0].parentNode;",item)
                    if p1_tagname == parent.tag_name:
                        p_attrs = {}
                        # butts
                        p_attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', parent)
                        if p_attrs.keys() == p_attrs1.keys():
                            final_items.append(item.get_attribute("innerHTML"))
                            print(item.get_attribute("innerHTML"))
                            print()
                # in case the item should be added but for some reason differs on one or two attributes
                # make note in instructions if the user isnt getting some desired result add it to one of the inputs
                elif attrs1.keys() != attrs2.keys():
                    parent = driver.execute_script("return arguments[0].parentNode;",item)
                    if p2_tagname == parent.tag_name:
                        p_attrs = {}
                        p_attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', parent)
                        if p_attrs.keys() == p_attrs1.keys():
                            final_items.append(item.get_attribute("innerHTML"))
                            print(item.get_attribute("innerHTML"))
                            print()

    #loop through the amount of result pages user wants
    for i in range(1, pages+1, 1):
        page_no = str(i)
        try:
            #find to next page
            driver.execute_script("arguments[0].click();",driver.find_element(By.LINK_TEXT,page_no))
            #go to next page
            URL = driver.current_url
            print(URL)
        except:
            print("An issue occurred with the scraping")
        #scrape
        scrape_url(URL)

    # getting the data in csv and json formats
    def get_data_csv_json(user_input):
        # convert list to csv and json if user answered yes
        if user_input == True:
            dict = {'Job Title': final_items}
            # csv
            df = pd.DataFrame(dict)
            df.to_csv('jobtitle.csv')
            # json
            json_str = json.dumps(dict, indent=1)
            with open('jobtitle2.json', 'w') as outfile:
                outfile.write(json_str)
                print("JSON file is created")
        else:
            breakpoint()

    #get_data_csv_json(get_data)

    driver.close()