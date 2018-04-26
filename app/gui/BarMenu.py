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
		# self.__create_view_menu()
		# self.__create_system_menu()
		# self.__create_help_menu()





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



		# #--- control center
		# control_center_action = QAction("Центр настроек", self.parent)
		# control_center_action.triggered.connect(lambda: lbus.emit(lbus.SHOW_CONTROL_CENTER))
		# control_center_action.setIcon(qficon("lock.png"))
		# control_center_action.setShortcut("Ctrl+1")
		# control_center_action.setWhatsThis("Цент настроек позволяет настроить параметры оборудования")
		# file_menu.addAction(control_center_action)
		#
		#
		# #--- settings
		# settings_action = QAction("Настройка конфигурации", self.parent)
		# # settings_action.triggered.connect(lambda: gbus.emit(gbus.SHOW_STANDART_SETTINGS))
		# settings_action.triggered.connect(lambda: lbus.emit(lbus.SHOW_SETTINGS))
		# settings_action.setIcon(qficon("window-new.png"))
		# settings_action.setShortcut("Ctrl+s")
		# file_menu.addAction(settings_action)
		# self.set_perm(settings_action, admin=True, guest=False, operator=False)
		#
		#
		# #--- orders
		# orders_action = QAction("Заказы", self.parent)
		# orders_action.triggered.connect(lambda: lbus.emit(lbus.SHOW_ORDERS_MODAL))
		# orders_action.setIcon(qficon("call-start.png"))
		# orders_action.setShortcut("Ctrl+o")
		# file_menu.addAction(orders_action)
		# self.set_perm(orders_action, admin=True, guest=False, operator=True)
		#
		# #--- users
		# # users_action = QAction("Пользователи", self.parent)
		# # users_action.triggered.connect(modal_actions.show_users_web)
		# # users_action.setIcon(qficon("contact-new.png"))
		# # # users_action.setShortcut("Ctrl+o")
		# # file_menu.addAction(users_action)
		# # self.set_perm(users_action, admin=True, guest=False, operator=False)
		#
		#
		# users_action = QAction("Пользователи", self.parent)
		# users_action.triggered.connect(lambda: gbus.emit(gbus.SHOW_USERS_MANAGER))
		# users_action.setIcon(qficon("contact-new.png"))
		# file_menu.addAction(users_action)
		# self.set_perm(users_action, admin=True, guest=False, operator=True)
		#
		#
		# #--- Режимы переворота бадьи - внешняя ссылка на web-проект
		# rmodes_action = QAction("Режимы переворота бадьи", self.parent)
		# rmodes_action.triggered.connect(lambda: gbus.emit(gbus.SHOW_BUCKET_ROTATION_MODES))
		# rmodes_action.setIcon(qficon("document-open-recent.png"))
		# file_menu.addAction(rmodes_action)
		# self.set_perm(rmodes_action, admin=True, guest=False, operator=True)
		#
		#
		# file_menu.addSeparator()
		#
		# #--- logout
		# # logout_action = QAction("Выход", self.parent)
		# logout_action = QAction("Сменить пользователя", self.parent)
		# logout_action.triggered.connect(self.__act_logout)
		# logout_action.setIcon(qficon("object-rotate-left.png"))
		# logout_action.setStatusTip("Сменить пользователя")
		# file_menu.addAction(logout_action)
		#
		#
		# file_menu.addSeparator()

		#--- act_hide
		add_todo_action = QAction("Новое", self.parent)
		# add_todo_action.setShortcut("Ctrl+Q")
		add_todo_action.setStatusTip("Новое задание")
		add_todo_action.setIcon(QIcon(get_icon("add.png")))
		add_todo_action.triggered.connect(self.parent.show_add_todo)
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
		exit_action.triggered.connect(self.parent.act_exit)
		file_menu.addAction(exit_action)


	#
	#
	# def __create_view_menu(self):
	# 	"""Вид"""
	#
	# 	#--- menu section
	# 	menu = self.menu.addMenu("Вид")
	#
	#
	# 	#--- ulog settings
	# 	ulog_settings_menu = QAction("Настройки журнала", self.parent)
	# 	ulog_settings_menu.setIcon(qficon("document-page-setup.png"))
	# 	ulog_settings_menu.triggered.connect(lambda: gbus.emit(gbus.SHOW_ULOG_SETTINGS))
	# 	menu.addAction(ulog_settings_menu)
	#
	#
	# 	#--- submenu iboxes
	# 	ibox_menu = QMenu(menu)
	# 	ibox_menu.setTitle("Информационные боксы")
	# 	ibox_menu.setIcon(qficon("view-list-icons-symbolic.png"))
	# 	menu.addMenu(ibox_menu)
	#
	# 	#--- создаём пункты подменю для информационных боксов
	# 	make_menus(ibox_menu)
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#

	#
	#
	#
	# def __create_help_menu(self):
	# 	"""Справка"""
	#
	#
	# 	help_menu = self.menu.addMenu("Справка")
	#
	# 	#--- about
	# 	help_menu_about = QAction("О программе", self.parent)
	# 	help_menu_about.setIcon(qficon("help-about.png"))
	# 	help_menu_about.triggered.connect(lambda: lbus.emit(lbus.SHOW_ABOUT))
	# 	help_menu.addAction(help_menu_about)
	#
	#
	# 	#--- documents
	# 	help_menu_documents = QAction("Документация", self.parent)
	# 	help_menu_documents.setIcon(qficon("document-open.png"))
	# 	help_menu_documents.triggered.connect(lambda: gbus.emit(gbus.SHOW_DOCUMENTS_SIMPLE))
	# 	help_menu.addAction(help_menu_documents)
	#
	#
	# 	#--- FAQ
	# 	help_menu_faq = QAction("Часто задаваемые вопросы", self.parent)
	# 	help_menu_faq.triggered.connect(lambda: gbus.emit(gbus.SHOW_DOCUMENTS_FAQ))
	# 	help_menu_faq.setIcon(qficon("call-start.png"))
	# 	help_menu.addAction(help_menu_faq)
	#
	#
	# #--- menu entries ---------------------------------------------------------
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#--- actions --------------------------------------------------------------

	def hide_window(self):
		self.parent.act_hide()
	#
	#
	# def __act_logout(self):
	# 	"""выход из под текущего аккаунта"""
	# 	if self.parent:
	# 		self.parent.logout()
	#
	# def __act_exit(self):
	# 	"""выход из приложения"""
	# 	if self.parent:
	# 		self.parent.act_exit()
	#
	#
	# def __start_modal_test_flags_line1(self):
	# 	"""отображение модала тестирования флажков линии 1"""
	# 	line_model = self.project.get_node("line1")
	# 	# modal_actions.show_modal_test_flags(line_model)
	# 	lbus.emit(lbus.SHOW_CALIBRATION_FLAGS, line_model)
	#
	# def __on_reload_server(self):
	# 	"""отправка сообщения на перезагрузку сервера"""
	# 	if self.parent:
	# 		self.parent.server.make_reload_request()
	#
	#
	# def __on_update_project_json(self):
	# 	"""скачать тек. версию project.json с сервера"""
	# 	update_file_project()
	#
	#
	# #
	# #
	# # def __open_rmodes_browser(self):
	# # 	"""Режимы переворота бадьи - внешняя ссылка на web-проект"""
	# #
	# # 	gbus.emit(gbus.SHOW_BUCKET_ROTATION_MODES)
	# #
	#
	# #
	# # def __open_users_manager(self):
	# # 	"""управление пользователями"""
	# # 	gbus.emit(gbus.SHOW_USERS_MANAGER)
	#
	#
	#
	# def __open_comlog_browser(self):
	# 	"""отобразить окно браузера с сервисом логирования"""
	# 	gbus.emit(gbus.SHOW_COMLOG_BROWSER)
	#
	#--- actions --------------------------------------------------------------
