#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from queue import Queue

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStyleFactory, QWidget, QHBoxLayout
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtCore import QTimer, pyqtSignal


# from ms3.net.PyTCP import ClientTcp
# from ms3.net.QReader import QReader
# from ms3.rc import get_font_path
# from ms3.shared import get_user
# from ms3.bus import dbus
# from ms3.data import def_ui
# from ms3.gui.modals.help_viewer import get_error_view
# from ms3.gui.system.req_res_modal import ReqResModal
# from ms3.gui.system.ModalInfoData import ModalInfoData

from .TasksList import TaskList
from .TasksControls import TaskControls
from .ModalEditTodo import ModalEditTodo

from ..storage import get_store

log = logging.getLogger("main")






class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		log.debug("инициализация главного окна программы")

		#--- заголовок окна
		self.title 		= "DTodo"

		#--- размеры
		self.max_x = 800
		self.max_y = 600

		#--- стиль окна
		# self.wstyle = ""

		#--- размер окна при старте
		# self.startup_size = def_ui.STUPTUP_SIZE_NORMAL


		self.bar_menu	= None			# меню


		#--- add fonts
		# QFontDatabase.addApplicationFont(get_font_path("Play-Bold.ttf"))
		# QFontDatabase.addApplicationFont(get_font_path("roboto", "RobotoRegular.ttf"))
		# QFontDatabase.addApplicationFont(get_font_path("roboto", "RobotoMono-Regular.ttf"))


		#--- FEATURES... ------------------------------------------------------
		#--- system tray
		#--- !!! KDE-error - при закрытии MainWindow трей остаётся висеть... и приложение не останавливается....
		#--- сейчас нагрузки на него нет - пока отключаем
		# tray = SystemTray(self)
		# tray.show()


		self.modal_edit_todo = None
		self.store = get_store()

		self.init_gui()
		self.set_todo_items()



	def init_gui(self):
		"""построение интерфейса"""

		#--- window meta
		self.setWindowTitle(self.title)
		self.setMinimumWidth(self.max_x)							# min width
		self.setMinimumHeight(self.max_y)


		#--- window style
		# styles = QStyleFactory.keys()
		# if self.wstyle in styles:
		# 	QApplication.setStyle(QStyleFactory.create(self.wstyle))


		# self.setGeometry(300, 300, 300, 300)


		self.main_widget = QWidget()
		self.setCentralWidget(self.main_widget)

		self.main_layout = QHBoxLayout()
		self.main_widget.setLayout(self.main_layout)


		self.tasks_list = TaskList()
		self.tasks_controls = TaskControls()
		self.tasks_controls.setMaximumWidth(200)
		self.tasks_controls.eadd.connect(self.show_add_todo)

		self.main_layout.addWidget(self.tasks_controls)
		self.main_layout.addWidget(self.tasks_list)

		# self.init_central_gui()


		#--- status bar
		self.statusBar().showMessage('')

		self.show()


	# def init_central_gui(self):
	# 	#--- mnemo bar
	# 	self.setCentralWidget(self.mnemo)



	def set_todo_items(self):
		self.tasks_list.set_items(self.store.items)


	def show_add_todo(self):
		self.modal_edit_todo = ModalEditTodo(self.on_save_todo, parent=self)
		self.modal_edit_todo.show()



	def on_save_todo(self, data_dict):

		store = get_store()
		store.add_item(data_dict)
		store.save()

		self.modal_edit_todo.close()
		self.modal_edit_todo = None

		self.set_todo_items()




	def act_exit(self):
		log.info("запрос на закрытие приложения")
		self.close()



	def closeEvent(self, QCloseEvent):
		"""перехват зактытия окна - предварительные завершения для объектов"""

		log.info("закрытие приложения - останавливаем процессы")


		log.info("закрытие приложения - выходим")
		QCloseEvent.accept()



