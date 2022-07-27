import crud
import web_scraper

pname = ""
URL = "https://www.geeksforgeeks.org/"
user_input1 = 'How to Apply For a Software Engineering Job in 4 Ways?'
user_input2 = 'How to prepare for ICFP or International Conference on Functional Programming?'
pages = 1
get_data = False
new_user_input = ""

#crud.create_project(pname,URL,user_input1,user_input2)
#pid=crud.read_project("TradeMe-Cars")
#crud.update_project(pid,pname,URL,user_input1,user_input2)
#crud.delete_project(pid)
#crud.read_all_projects()

web_scraper.scrape(URL,user_input1,user_input2, pages, get_data)
