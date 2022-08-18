import crud
import web_scraper

pname = ""
URL = "https://www.seek.co.nz/jobs-in-information-communication-technology"
user_input1 = 'Service Desk Analyst'
user_input2 = 'Systems Engineer Queenstown'
pages = 1
new_user_input = ""
test = {'Age': [52, 24, 31, 47, 51, 61],
        'Sex': ['F', 'M', 'M', 'F', 'F', 'M'],
        'height': [143, 163, 144, 154, 174, 177],
        'weight': [77, 66, 59, 53, 71, 63], }
#crud.create_project(pname,URL,user_input1,user_input2)
# pid=crud.read_project("geeks4geeks")
#crud.update_project(pid,pname,URL,user_input1,user_input2)
#crud.delete_project(pid)
#crud.read_all_projects()

web_scraper.scrape(URL,user_input1,user_input2, pages)
# web_scraper.get_data_csv_json("csv",test,"test")
# crud.read_user_input(pid)