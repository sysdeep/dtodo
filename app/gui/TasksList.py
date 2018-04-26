#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QVBoxLayout, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal

from app.rc import get_priority_icon

class TaskList(QWidget):
	eedit = pyqtSignal(str)
	eremove = pyqtSignal(str)
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

		self.__make_cmenu()




	def __make_cmenu(self):
		"""контекстное меню"""
		self.list.setContextMenuPolicy(Qt.ActionsContextMenu)
		edit 	= QAction("Изменить", self.list)
		remove 	= QAction("Удалить", self.list)
		# create_new_parent 	= QAction("Новая запись для данного элемента", self)
		# create_new_level 	= QAction("Новая запись такого же уровня", self)
		#
		# edit_name 			= QAction("Изменить название", self)
		# edit_icon 			= QAction("Изменить иконки", self)
		# show_info 			= QAction("Информация", self)
		# # act_copy 			= QAction("Копировать", self)
		# # act_paste 			= QAction("Вставить", self)
		#
		# move_up				= QAction("Выше", self)
		# move_down			= QAction("Ниже", self)
		#
		# remove_item 		= QAction("Удалить запись(ветку)", self)
		#
		# separator1 = QAction(self)
		# separator1.setSeparator(True)
		#
		# separator2 = QAction(self)
		# separator2.setSeparator(True)
		#
		# separator3 = QAction(self)
		# separator3.setSeparator(True)

		self.list.addAction(edit)
		self.list.addAction(remove)
		# self.addAction(create_new_parent)
		# self.addAction(create_new_level)
		# self.addAction(separator1)
		# self.addAction(edit_name)
		# self.addAction(edit_icon)
		# self.addAction(show_info)
		# # self.addAction(act_copy)
		# # self.addAction(act_paste)
		#
		# self.addAction(separator2)
		#
		# self.addAction(move_up)
		# self.addAction(move_down)
		#
		# self.addAction(separator3)
		#
		# self.addAction(remove_item)
		# # self.addSeparetor()


		# create_new_root.setIcon(qicon("filesystems", "folder_blue.png"))
		# create_new_parent.setIcon(qicon("filesystems", "folder_green.png"))
		# create_new_level.setIcon(qicon("filesystems", "folder_orange.png"))
		# edit_name.setIcon(qicon("actions", "edit.png"))
		# edit_icon.setIcon(qicon("actions", "frame_image.png"))
		# show_info.setIcon(qicon("actions", "kdeprint_printer_infos.png"))
		# # act_copy.setIcon(qicon("actions", "editcopy.png"))
		# remove_item.setIcon(qicon("actions", "remove.png"))
		#
		# move_up.setIcon(qicon("actions", "arrow_up.png"))
		# move_down.setIcon(qicon("actions", "arrow_down.png"))
		#
		# create_new_root.triggered.connect(self.__act_create_new_root)
		# create_new_parent.triggered.connect(self.__act_create_new_parent)
		# create_new_level.triggered.connect(self.__act_create_new_level)
		# edit_name.triggered.connect(self.__act_edit_name)
		# edit_icon.triggered.connect(self.__act_edit_icon)
		# show_info.triggered.connect(self.__act_show_info)
		# act_copy.triggered.connect(self.__act_copy)
		# act_paste.triggered.connect(self.__act_paste)

		# move_up.triggered.connect(self.__act_move_up)
		# move_down.triggered.connect(self.__act_move_down)

		edit.triggered.connect(lambda x: self.show_edit())
		remove.triggered.connect(lambda x: self.show_remove())





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
		self.eedit.emit(self.current_item_id)


	def show_remove(self):
		self.eremove.emit(self.current_item_id)