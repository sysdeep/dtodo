#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QVBoxLayout

class TaskList(QWidget):
	def __init__(self, parent=None):
		super(TaskList, self).__init__(parent)

		self.main_layout = QVBoxLayout(self)
		self.list = QListWidget()

		self.main_layout.addWidget(self.list)


		item = QListWidgetItem("first")
		self.list.addItem(item)



	def set_items(self, items_obj):

		self.list.clear()

		for item in items_obj:
			self.__append_item(item)





	def __append_item(self, item):
		list_item = QListWidgetItem(item.text)
		self.list.addItem(list_item)


