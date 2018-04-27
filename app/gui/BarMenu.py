#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Главное меню

	Доступ к меню:
		для ограничения доступа к меню создан спец. объект MPerm, в него заносятся те меню, которые надо контролировать:
			mperm.append(menu_entry, admin=True, guest=False, operator=False) - доступ только для админа

		при инициализации и любом обновлении доступа - необходимо данный список обновить:
			mperm.check_all(admin=True, guest=False, operator=False)
		для обновления передаются текущие флаги пользователя. При инициализации они все будут False

		далее подключаемся к каналу изменений пользователя, и при изменении - перепроверить все элементы
"""
from PyQt5.QtWidgets import QAction, QShortcut, QMenu
from PyQt5.QtGui import QKeySequence, QIcon

from app.rc import get_icon










class BarMenu(object):
	"""Главное меню"""
	def __init__(self, parent):
		self.parent = parent

		#--- menu obj
		self.menu = self.parent.menuBar()


		#--- create menu entries
		self.__create_file_menu()
		self.__create_help_menu()





		#
		# #--- сочетания клавищ
		# #-- скрытое сочетание для запуска модала смены доступа
		# sq = QShortcut(QKeySequence("Ctrl+r"), self.parent)
		# # sq.activated.connect(modal_actions.show_modal_user_roles)
		# sq.activated.connect(lambda: gbus.emit(gbus.SHOW_USER_ROLES))



	#--- menu entries ---------------------------------------------------------
	def __create_file_menu(self):
		"""File"""

		file_menu = self.menu.addMenu("Файл")





		#--- act_hide
		add_todo_action = QAction("Добавить", self.parent)
		# add_todo_action.setShortcut("Ctrl+Q")
		add_todo_action.setStatusTip("Новое задание")
		add_todo_action.setIcon(QIcon(get_icon("add.png")))
		add_todo_action.triggered.connect(self.show_add_todo)
		file_menu.addAction(add_todo_action)


		#--- act_hide
		hide_action = QAction("Скрыть", self.parent)
		# hide_action.setShortcut("Ctrl+Q")
		hide_action.setStatusTip("Скрыть приложение")
		hide_action.setIcon(QIcon(get_icon("close_hide.png")))
		hide_action.triggered.connect(self.hide_window)
		file_menu.addAction(hide_action)

		file_menu.addSeparator()

		#--- act_exit
		exit_action = QAction("&Закрыть", self.parent)
		exit_action.setShortcut("Ctrl+Q")
		exit_action.setStatusTip("Закрыть приложение")
		exit_action.setIcon(QIcon(get_icon("delete.png")))
		exit_action.triggered.connect(self.exit)
		file_menu.addAction(exit_action)



	def __create_help_menu(self):
		"""Справка"""


		help_menu = self.menu.addMenu("Справка")

		#--- about
		help_menu_about = QAction("О программе", self.parent)
		help_menu_about.setIcon(QIcon(get_icon("about.png")))
		help_menu_about.triggered.connect(self.show_about)
		help_menu.addAction(help_menu_about)










	#--- actions --------------------------------------------------------------

	def hide_window(self):
		self.parent.act_hide()

	def exit(self):
		self.parent.act_exit()

	def show_add_todo(self):
		self.parent.show_add_todo()

	def show_about(self):
		self.parent.show_modal_about()

	#--- actions --------------------------------------------------------------
