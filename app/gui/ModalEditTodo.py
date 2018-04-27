#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QDialog, QPushButton, QHBoxLayout, QVBoxLayout, \
	QGridLayout, QGroupBox, QTabWidget, QWidget, QScrollArea, QFormLayout, QLineEdit, QComboBox, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

from app.rc import get_icon, get_priority_icon, get_status_icon


from app.data import TODO_STATUSES, TODO_PRIORITYES

class ModalEditTodo(QDialog):
	def __init__(self, edata, cb, parent=None):
		super(ModalEditTodo, self).__init__(parent)

		self.setFixedHeight(300)
		self.setFixedWidth(400)

		self.setWindowTitle("Редактирование записи")

		self.cb = cb

		self.main_layout = QVBoxLayout(self)


		self.form = QFormLayout()
		self.main_layout.addLayout(self.form)


		self.tid = edata["id"]
		self.edata = edata


		self.edit_text = QLineEdit()
		self.form.addRow("текст", self.edit_text)

		self.edit_statuses = QComboBox()
		self.form.addRow("статус", self.edit_statuses)

		self.edit_priority = QComboBox()
		self.form.addRow("приоритет", self.edit_priority)



		self.edit_description = QTextEdit()
		self.main_layout.addWidget(self.edit_description)



		self.st_int = []
		self.st_str = []

		for st in sorted(TODO_STATUSES.keys()):
			self.st_int.append(st)
			self.st_str.append(TODO_STATUSES[st])

		# self.edit_statuses.addItems(self.st_str)
		for index, item in enumerate(self.st_str):
			icon_name = self.st_int[index]
			icon = QIcon(get_status_icon(icon_name))
			self.edit_statuses.addItem(icon, item)


		self.pr_int = []
		self.pr_str = []

		for pr in sorted(TODO_PRIORITYES.keys()):
			self.pr_int.append(pr)
			self.pr_str.append(TODO_PRIORITYES[pr])


		for index, item in enumerate(self.pr_str):
			icon_name = self.pr_int[index]
			icon = QIcon(get_priority_icon(icon_name))
			self.edit_priority.addItem(icon, item)


		controls = QHBoxLayout()
		self.main_layout.addLayout(controls)


		btn_close = QPushButton("Закрыть")
		btn_close.setIcon(QIcon(get_icon("delete.png")))
		btn_close.clicked.connect(self.close)


		btn_save = QPushButton("Сохранить")
		btn_save.setIcon(QIcon(get_icon("save.png")))
		btn_save.clicked.connect(self.save)


		controls.addStretch()
		controls.addWidget(btn_save)
		controls.addWidget(btn_close)


		self.load_data()



	def load_data(self):
		self.edit_text.setText(self.edata["text"])

		status_index = self.st_int.index(self.edata["status"])
		self.edit_statuses.setCurrentIndex(status_index)

		priority_index = self.pr_int.index(self.edata["priority"])
		self.edit_priority.setCurrentIndex(priority_index)

		self.edit_description.setText(self.edata["description"])



	def save(self):

		status_index = self.edit_statuses.currentIndex()
		status = self.st_int[status_index]

		priority_index = self.edit_priority.currentIndex()
		priority = self.pr_int[priority_index]

		data = {
			"id"		: self.tid,
			"text"		: self.edit_text.text(),
			"status"	: status,
			"priority"	: priority,
			"description"	: self.edit_description.toPlainText()
		}


		if self.cb:
			self.cb(data)












if __name__ == "__main__":

	import sys
	from PyQt5.QtWidgets import QApplication
	from ..storage.Item import Item


	app = QApplication(sys.argv)


	item = Item()
	item.status = 3
	data_dict = item.dump()

	dialog = ModalEditTodo(data_dict, lambda data: print(data))
	dialog.show()


	# view.show()



	sys.exit(app.exec_())