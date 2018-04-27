#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QVBoxLayout, QAction, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal

from app.rc import get_priority_icon, get_icon, get_status_icon
from app.data import TODO_STATUSES, TODO_PRIORITYES

class TaskList(QWidget):
	eedit = pyqtSignal(str)
	eremove = pyqtSignal(str)
	estatus = pyqtSignal(str, int)
	epriority = pyqtSignal(str, int)
	def __init__(self, parent=None):
		super(TaskList, self).__init__(parent)

		self.status_code = 0
		self.status_text = ""
		self.items_count = 0

		self.main_layout = QVBoxLayout(self)
		self.list = QListWidget()
		self.list.itemDoubleClicked.connect(self.on_dbl_clicked)
		# self.list.itemClicked.connect(self.on_select)
		self.list.pressed.connect(self.on_select)

		self.main_layout.addWidget(self.list)


		self.current_item_id = ""

		# self.__make_cmenu()
		self.list.contextMenuEvent = self.show_cmenu


	def show_cmenu(self, event):

		menu = QMenu()

		edit 	= QAction("Изменить", self)
		edit.setIcon(QIcon(get_icon("edit.png")))



		remove 	= QAction("Удалить", self)
		remove.setIcon(QIcon(get_icon("delete.png")))

		menu.addAction(edit)
		menu.addSeparator()


		statuses 	= QMenu("Изменить статус")
		statuses.setIcon(QIcon(get_icon("edit.png")))
		menu.addMenu(statuses)

		for st_int in sorted(TODO_STATUSES.keys()):
			st_str = TODO_STATUSES[st_int]
			action = QAction(st_str, self)
			action.setIcon(QIcon(get_status_icon(st_int)))
			action.triggered.connect(lambda x, z=st_int: self.change_status(z))
			statuses.addAction(action)



		priority 	= QMenu("Изменить приоритет")
		priority.setIcon(QIcon(get_icon("edit.png")))
		menu.addMenu(priority)

		for pr_int in sorted(TODO_PRIORITYES.keys()):
			pr_str = TODO_PRIORITYES[pr_int]
			action = QAction(pr_str, self)
			action.setIcon(QIcon(get_priority_icon(pr_int)))
			action.triggered.connect(lambda x, z=pr_int: self.change_priority(z))
			priority.addAction(action)


		menu.addSeparator()
		menu.addAction(remove)


		action = menu.exec_(event.globalPos())
		# action = menu.exec_(event)


		if action == edit:
			self.show_edit()
		elif action == remove:
			self.show_remove()
		else:
			pass




	def get_name(self):
		return "{} [{}]".format(self.status_text, self.items_count)


	def clear_list(self):
		self.items_count = 0
		self.current_item_id = None
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
		icon = QIcon(get_priority_icon(item.priority))
		list_item = QListWidgetItem(item.text)
		list_item.setIcon(icon)
		list_item.setData(Qt.UserRole + 1, item.id)
		self.list.addItem(list_item)





	def on_select(self, list_item):
		id = list_item.data(Qt.UserRole + 1)
		self.current_item_id = id


	def on_dbl_clicked(self, list_item):
		id = list_item.data(Qt.UserRole + 1)
		self.current_item_id = id
		self.show_edit()


	def show_edit(self):
		if self.current_item_id:
			self.eedit.emit(self.current_item_id)


	def show_remove(self):
		if self.current_item_id:
			self.eremove.emit(self.current_item_id)


	def change_status(self, status_code):
		if self.current_item_id:
			self.estatus.emit(self.current_item_id, status_code)


	def change_priority(self, p_code):
		if self.current_item_id:
			self.epriority.emit(self.current_item_id, p_code)











#--- old cmenu ----------------------------------------------------------------
	# def __make_cmenu(self):
	# 	"""контекстное меню"""
	# 	self.list.setContextMenuPolicy(Qt.ActionsContextMenu)
	# 	edit 	= QAction("Изменить", self.list)
	# 	edit.setIcon(QIcon(get_icon("edit.png")))
	#
	# 	remove 	= QAction("Удалить", self.list)
	# 	remove.setIcon(QIcon(get_icon("delete.png")))
	#
	# 	separator1 = QAction(self)
	# 	separator1.setSeparator(True)
	#
	# 	self.list.addAction(edit)
	# 	self.list.addAction(separator1)
	# 	self.list.addAction(remove)
	#
	#
	# 	edit.triggered.connect(lambda x: self.show_edit())
	# 	remove.triggered.connect(lambda x: self.show_remove())
#--- old cmenu ----------------------------------------------------------------