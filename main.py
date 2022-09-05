
import crud
import web_scraper

test = {'Age': [52, 24, 31, 47, 51, 61],
        'Sex': ['F', 'M', 'M', 'F', 'F', 'M'],
        'height': [143, 163, 144, 154, 174, 177],
        'weight': [77, 66, 59, 53, 71, 63], }
pname = "test"
URL = "https://www.trademe.co.nz/a/jobs/search?search_string=software%20developer"
URL_2 = ""
user_input1 = 'Front End / Back End / Full Stack Development Jobs'
user_input2 = 'CONTRACT React Native Mobile Developer'
pages = 1
new_user_input = ""

# crud.create_project("JCRFrJoufgwbbDhyuMaQ",pname,URL,URL_2)
# pid=crud.read_project("geeks4geeks")
# crud.update_project(pid,pname,URL,user_input1,user_input2)
# crud.delete_project(pid)
# crud.read_all_projects()
# check = web_scraper.check_inputs(URL,user_input1,user_input2)
# print(check)
# web_scraper.scrape(URL,user_input1,user_input2, pages)
# web_scraper.get_data_csv_json("csv", test, "test", URL)
# crud.read_user_input(pid)
