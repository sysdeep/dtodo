#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStyleFactory, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QTabWidget, QLineEdit
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtCore import QTimer, pyqtSignal



from .TasksList import TaskList
from .ModalEditTodo import ModalEditTodo
from .ModalAbout import ModalAbout
from .SystemTray import SystemTray
from .BarMenu import BarMenu

from ..storage import get_store
from ..rc import get_media, get_icon, get_status_icon
from .. import data

log = logging.getLogger("main")






class MainWindow(QMainWindow):
	bus = pyqtSignal(str)

	def __init__(self):
		super(MainWindow, self).__init__()

		log.debug("инициализация главного окна программы")

		#--- заголовок окна
		self.title 		= "DTodo"

		#--- размеры
		self.max_x = 600
		self.max_y = 400

		#--- стиль окна
		# self.wstyle = ""

		#--- размер окна при старте
		# self.startup_size = def_ui.STUPTUP_SIZE_NORMAL


		self.bar_menu	= BarMenu(parent=self)			# меню


		#--- add fonts
		# QFontDatabase.addApplicationFont(get_font_path("Play-Bold.ttf"))
		# QFontDatabase.addApplicationFont(get_font_path("roboto", "RobotoRegular.ttf"))
		# QFontDatabase.addApplicationFont(get_font_path("roboto", "RobotoMono-Regular.ttf"))



		#--- system tray
		tray_icon = QIcon(get_media("tray.png"))
		tray = SystemTray(tray_icon, parent=self)
		tray.show()


		self.modal_edit_todo = None
		self.edit_todo_is_new = False
		self.store = get_store()
		self.tabs_map = {}						# {status_code: widget}
		self.current_status_code = 0

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

		self.main_layout = QVBoxLayout()
		# self.main_layout.setContentsMargins(0,0,0,0)
		self.main_widget.setLayout(self.main_layout)



		self.tabs = QTabWidget()
		self.tabs.currentChanged.connect(self.on_tab_changed)
		self.main_layout.addWidget(self.tabs)

		index = 0
		for st in sorted(data.TODO_STATUSES.keys()):
			todo_list = TaskList()
			self.tabs_map[st] = todo_list
			todo_list.eedit.connect(self.show_edit_todo)
			todo_list.eremove.connect(self.show_remove_todo)
			todo_list.estatus.connect(self.change_todo_status)
			todo_list.epriority.connect(self.change_todo_priority)
			todo_list.status_code = st
			todo_list.status_text = data.TODO_STATUSES[st]
			self.tabs.addTab(todo_list, todo_list.get_name())
			self.tabs.setTabIcon(index, QIcon(get_status_icon(st)))
			index += 1


		# for tab_item in self.tabs.i


		controls = QHBoxLayout()
		self.main_layout.addLayout(controls)

		btn_hide = QPushButton("Скрыть")
		btn_hide.setIcon(QIcon(get_icon("close_hide.png")))
		btn_hide.clicked.connect(self.act_hide)

		# btn_quit = QPushButton("Закрыть")
		# btn_quit.setIcon(QIcon(get_icon("delete.png")))
		# btn_quit.clicked.connect(self.act_exit)

		btn_add = QPushButton("Добавить")
		btn_add.setIcon(QIcon(get_icon("add.png")))
		btn_add.clicked.connect(self.show_add_todo)



		# edit_new_todo = QLineEdit()
		# btn_add_new_todo = QPushButton("add")
		#
		#
		# controls.addWidget(edit_new_todo)
		# controls.addWidget(btn_add_new_todo)
		controls.addStretch()
		controls.addWidget(btn_add)
		controls.addWidget(btn_hide)
		# controls.addWidget(btn_quit)


		#--- status bar
		# self.statusBar().showMessage('')

		# self.show()

		self.act_show()

	# def init_central_gui(self):
	# 	#--- mnemo bar
	# 	self.setCentralWidget(self.mnemo)



	def set_todo_items(self):

		for w in self.tabs_map.values():
			w.clear_list()

		for item in self.store.items:
			st = item.status
			if not st in self.tabs_map:
				continue
			w = self.tabs_map[st]
			w.append_item(item)

		# self.tasks_list.set_items(self.store.items)

		for w in self.tabs_map.values():
			tab_index = self.tabs.indexOf(w)
			self.tabs.setTabText(tab_index, w.get_name())





	def show_remove_todo(self, item_id):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Подтверждение удаления")
		msg.setText("Вы действительно хотите удалить элемент?")
		# msg.setInformativeText(message)
		msg.addButton("Удалить", QMessageBox.AcceptRole)
		msg.addButton("Отмена", QMessageBox.RejectRole)

		result = msg.exec_()

		if result == QMessageBox.AcceptRole:
			self.store.remove_item(item_id)
			self.store.save()
			self.set_todo_items()
		else:
			print("reject")



	def change_todo_status(self, tid, status_code):
		data_dict = {
			"id"		: tid,
			"status"	: status_code
		}

		self.store.update_item(data_dict)
		self.store.save()

		self.set_todo_items()


	def change_todo_priority(self, tid, priority_code):
		data_dict = {
			"id"		: tid,
			"priority"	: priority_code
		}

		self.store.update_item(data_dict)
		self.store.save()

		self.set_todo_items()



	def show_edit_todo(self, id):
		self.edit_todo_is_new = False
		item = self.store.find_id(id)
		self.__show_modal_edit_todo(item)



	def show_add_todo(self):
		self.edit_todo_is_new = True
		item = self.store.find_id(None)				# new instance
		item.status = self.current_status_code
		self.__show_modal_edit_todo(item)



	def __show_modal_edit_todo(self, item):
		data_dict = item.dump()
		self.modal_edit_todo = ModalEditTodo(data_dict, self.on_save_todo, parent=self)
		self.modal_edit_todo.show()


	def on_save_todo(self, data_dict):

		if self.edit_todo_is_new:
			self.store.add_item(data_dict)
		else:
			self.store.update_item(data_dict)

		self.store.save()

		# store = get_store()
		# store.add_item(data_dict)
		# store.save()

		self.modal_edit_todo.close()
		self.modal_edit_todo = None

		self.set_todo_items()




	def show_modal_about(self):
		ModalAbout(self).show()




	def act_hide(self):
		"""скрыть главное окно"""

		self.hide()
		self.bus.emit("hidden")


	def act_show(self):
		"""отобразить главное окно"""

		self.show()
		self.bus.emit("showed")




	def on_tab_changed(self, index):
		"""переключение таба - сохраняем статус(для модала создания)"""
		w = self.tabs.currentWidget()
		self.current_status_code = w.status_code



	def act_exit(self):
		log.info("запрос на закрытие приложения")
		# self.close()
		QApplication.instance().quit()
		# self.quit()

	def closeEvent(self, QCloseEvent):
		"""перехват зактытия окна - предварительные завершения для объектов"""

		self.act_hide()
		QCloseEvent.ignore()

		# log.info("закрытие приложения - останавливаем процессы")
		#
		#
		# log.info("закрытие приложения - выходим")
		# QCloseEvent.accept()



