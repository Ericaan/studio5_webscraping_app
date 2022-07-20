import crud
import web_scraper

pname = ""
URL = "https://www.geeksforgeeks.org/"
user_input1 = 'How to Write a Powerful Resume 2022 '
user_input2 = 'Top Data Structures That Every Programmer Must Know'
pages = 1
get_data = False
new_user_input = ""

#crud.create_project(pname,URL,user_input1,user_input2)
#pid=crud.read_project("TradeMe-Cars")
#crud.update_project(pid,pname,URL,user_input1,user_input2)
#crud.delete_project(pid)
#crud.read_all_projects()

web_scraper.scrape(URL,user_input1,user_input2, pages, get_data)
