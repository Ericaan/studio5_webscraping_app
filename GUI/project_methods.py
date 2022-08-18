
from PyQt5 import QtCore, QtWidgets
import crud


# buttons and other interaction methods
# refresh the table so the column titles match the template
def table_refresh(tableWidget, tree_template):
    # clear the table first
    while tableWidget.columnCount() > 0:
        tableWidget.removeColumn(0)
    # now iterate over the tree widget
    iterator = QtWidgets.QTreeWidgetItemIterator(tree_template)
    while iterator.value():
        item = iterator.value()
        if item.parent() is None:
            # column
            item_1 = QtWidgets.QTableWidgetItem()
            cols = tableWidget.columnCount()
            tableWidget.setColumnCount(cols + 1)
            tableWidget.setHorizontalHeaderItem(cols, item_1)
            tableWidget.horizontalHeaderItem(cols).setText(item.text(0))
            # row 1 item
            item_2 = QtWidgets.QTableWidgetItem()
            tableWidget.setItem(0, cols, item_2)
            tableWidget.item(0, cols).setText(item.text(1))
            # row 2 item
            item_3 = QtWidgets.QTableWidgetItem()
            tableWidget.setItem(1, cols, item_3)
            tableWidget.item(1, cols).setText(item.text(2))
        else:
            # column
            item_1 = QtWidgets.QTableWidgetItem()
            cols = tableWidget.columnCount()
            tableWidget.setColumnCount(cols + 1)
            tableWidget.setHorizontalHeaderItem(cols, item_1)
            tableWidget.horizontalHeaderItem(cols).setText(item.parent().text(0) + "_" + item.text(0))
            # row 1 item
            item_2 = QtWidgets.QTableWidgetItem()
            tableWidget.setItem(0, cols, item_2)
            tableWidget.item(0, cols).setText(item.text(1))
            # row 2 item
            item_3 = QtWidgets.QTableWidgetItem()
            tableWidget.setItem(1, cols, item_3)
            tableWidget.item(1, cols).setText(item.text(2))
        iterator += 1


# saves/updates the project to the database
def save_click(lbl_pname, url_bar, url_bar2, temp_dict):
    pid = crud.read_project(lbl_pname.text())
    pname = lbl_pname.text()
    purl = url_bar.toPlainText()
    purl2 = url_bar2.toPlainText()
    pinput = temp_dict
    crud.update_project(pid, pname, purl, purl2, pinput)
    temp_dict.clear()


# makes the template into a dictionary that can be saved more easily onto the database
def make_dict(tree_template, temp_dict):
    iterator = QtWidgets.QTreeWidgetItemIterator(tree_template)
    while iterator.value():
        item = iterator.value()
        if item.parent() is None:
            key = item.text(0)
            values = [item.text(1), item.text(2)]
            temp_dict[key] = values
        else:
            key = item.parent().text(0)
            values = {item.text(0): [item.text(1), item.text(2)]}
            temp_dict[key].append(values)
        iterator += 1


# navigate method for go button
def navigate(url, bar, brows):
    # in case it doesnt have http
    if not url.startswith("http"):
        url = "http://" + url
        bar.setText(url)
    brows.setUrl(QtCore.QUrl(url))


# delete item from template and preview table
def del_temp_item(tree_template, rb_delete):
    item = tree_template.currentItem()
    root = tree_template.invisibleRootItem()
    if rb_delete.isChecked():
        (item.parent() or root).removeChild(item)


# adding a new item to the template
def new_branch(rb_select, rb_rel_select, tree_template, txt_input1, txt_input2, tableWidget):
    if rb_select.isChecked():
        # declare a new tree widget item
        QtWidgets.QTreeWidgetItem(tree_template)
        count = tree_template.topLevelItemCount()
        # set new tree widget item
        tree_template.topLevelItem(count - 1).setText(0, "newItem")
        tree_template.topLevelItem(count - 1).setText(1, txt_input1.toPlainText())
        tree_template.topLevelItem(count - 1).setText(2, txt_input2.toPlainText())
        tree_template.topLevelItem(count - 1).setFlags(
            tree_template.topLevelItem(count - 1).flags() | QtCore.Qt.ItemIsEditable)
        # table update
        # column
        item_1 = QtWidgets.QTableWidgetItem()
        cols = tableWidget.columnCount()
        tableWidget.setColumnCount(cols + 1)
        tableWidget.setHorizontalHeaderItem(cols, item_1)
        tableWidget.horizontalHeaderItem(cols).setText("newItem")
        # row 1 item
        item_2 = QtWidgets.QTableWidgetItem()
        tableWidget.setItem(0, cols, item_2)
        tableWidget.item(0, cols).setText(txt_input1.toPlainText())
        # row 2 item
        item_3 = QtWidgets.QTableWidgetItem()
        tableWidget.setItem(1, cols, item_3)
        tableWidget.item(1, cols).setText(txt_input2.toPlainText())
    elif rb_rel_select.isChecked():
        # find the item its relatively selected to
        item = tree_template.selectedItems()
        # set the new tree widget item
        the_child = QtWidgets.QTreeWidgetItem()
        the_child.setText(0, "newSubItem")
        the_child.setText(1, txt_input1.toPlainText())
        the_child.setText(2, txt_input2.toPlainText())
        the_child.setFlags(the_child.flags() | QtCore.Qt.ItemIsEditable)
        item[0].addChild(the_child)
        # table update
        # column
        item_1 = QtWidgets.QTableWidgetItem()
        cols = tableWidget.columnCount()
        tableWidget.setColumnCount(cols + 1)
        tableWidget.setHorizontalHeaderItem(cols, item_1)
        tableWidget.horizontalHeaderItem(cols).setText(item[0].text(0) + "newSubItem")
        # row 1 item
        item_2 = QtWidgets.QTableWidgetItem()
        tableWidget.setItem(0, cols, item_2)
        tableWidget.item(0, cols).setText(txt_input1.toPlainText())
        # row 2 item
        item_3 = QtWidgets.QTableWidgetItem()
        tableWidget.setItem(1, cols, item_3)
        tableWidget.item(1, cols).setText(txt_input2.toPlainText())


# delete the project from the database
def del_project(lbl_pname):
    pid = crud.read_project(lbl_pname.text())
    crud.delete_project(pid)
