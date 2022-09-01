from PyQt5 import QtWidgets

import crud
import web_scraper

# import numpy as np
# from pyqtgraph.pgcollections import OrderedDict
# listOfTuples = [('text_%d' % i, i, i / 9.) for i in range(12)]
# listOfLists = [list(row) for row in listOfTuples]
# plainArray = np.array(listOfLists, dtype=object)
# recordArray = np.array(listOfTuples, dtype=[('string', object),
#                                             ('integer', int),
#                                             ('floating', float)])
# dictOfLists = OrderedDict([(name, list(recordArray[name])) for name in recordArray.dtype.names])
# listOfDicts = [OrderedDict([(name, rec[name]) for name in recordArray.dtype.names]) for rec in recordArray]
# transposed = [[row[col] for row in listOfTuples] for col in range(len(listOfTuples[0]))]
# test = {'Age': [52, 24, 31, 47, 51, 61],
#         'Sex': ['F', 'M', 'M', 'F', 'F', 'M'],
#         'height': [143, 163, 144, 154, 174, 177],
#         'weight': [77, 66, 59, 53, 71, 63], }
#
# from PyQt5 import QtWidgets
# from pyqtgraph import PlotWidget, plot
# import pyqtgraph as pg
# import sys  # We need sys so that we can pass argv to QApplication
# import os
#
# class MainWindow(QtWidgets.QMainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#
#         self.graphWidget = pg.TableWidget()
#         self.setCentralWidget(self.graphWidget)
#
#         hour = [1,2,3,4,5,6,7,8,9,10]
#         temperature = [30,32,34,32,33,31,29,32,35,45]
#
#
#         self.graphWidget.setData(test)
#
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     main = MainWindow()
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
# df = pd.read_csv('softdev.csv')
# df["mytext_new"] = df['Job Title'].str.lower().str.replace('[^\w\s]', '')
#
# new_df = df.mytext_new.str.split(expand=True).stack().value_counts().reset_index()
#
# new_df.columns = ['Word', 'Frequency']
#
# print(len(new_df))




# pname = "test"
# URL = "https://www.trademe.co.nz/a/jobs/search?search_string=software%20developer"
# URL_2 = ""
# user_input1 = 'Front End / Back End / Full Stack Development Jobs'
# user_input2 = 'CONTRACT React Native Mobile Developer'
# pages = 1
# new_user_input = ""
# crud.create_project("JCRFrJoufgwbbDhyuMaQ",pname,URL,URL_2)
# pid=crud.read_project("geeks4geeks")
#crud.update_project(pid,pname,URL,user_input1,user_input2)
#crud.delete_project(pid)
#crud.read_all_projects()
# check = web_scraper.check_inputs(URL,user_input1,user_input2)
# print(check)
# web_scraper.scrape(URL,user_input1,user_input2, pages)
# web_scraper.get_data_csv_json("csv", test, "test", URL)
# crud.read_user_input(pid)
