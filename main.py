import crud
import web_scraper

pname = ""
URL = "https://www.seek.co.nz/jobs-in-community-services-development"
user_input1 = 'Youth Worker'
user_input2 = 'Case Manager'
pages = 2
get_data = False
new_user_input = ""

#crud.create_project(pname,URL,user_input1,user_input2)
#pid=crud.read_project("TradeMe-Cars")
#crud.update_project(pid,pname,URL,user_input1,user_input2)
#crud.delete_project(pid)
#crud.read_all_projects()

web_scraper.scrape(URL,user_input1,user_input2, pages, get_data)
