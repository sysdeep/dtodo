#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal

class TaskList(QWidget):
	eedit = pyqtSignal(str)
	def __init__(self, parent=None):
		super(TaskList, self).__init__(parent)

		self.status_code = 0
		self.status_text = ""
		self.items_count = 0

		self.main_layout = QVBoxLayout(self)
		self.list = QListWidget()
		self.list.itemDoubleClicked.connect(self.show_edit)

		self.main_layout.addWidget(self.list)



	def get_name(self):
		return "{} [{}]".format(self.status_text, self.items_count)


	def clear_list(self):
		self.items_count = 0
		self.list.clear()


	def append_item(self, item_obj):
		self.items_count += 1
		self.__append_item(item_obj)

	# def set_items(self, items_obj):
	#
	# 	self.list.clear()
	#
	# 	for item in items_obj:
	# 		self.__append_item(item)





	def __append_item(self, item):
		list_item = QListWidgetItem(item.text)
		list_item.setData(Qt.UserRole + 1, item.id)
		self.list.addItem(list_item)





	def show_edit(self, list_item):
		id = list_item.data(Qt.UserRole + 1)
		self.eedit.emit(id)