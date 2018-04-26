#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QTabWidget, QWidget, QScrollArea, QFormLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ModalEditTodo(QDialog):
	def __init__(self, cb, parent=None):
		super(ModalEditTodo, self).__init__(parent)

		self.setFixedHeight(300)
		self.setFixedWidth(400)

		self.setWindowTitle("Редактирование записи")

		self.cb = cb

		self.main_layout = QVBoxLayout(self)


		self.form = QFormLayout()
		self.main_layout.addLayout(self.form)



		self.edit_text = QLineEdit()
		self.form.addRow("text", self.edit_text)




		controls = QHBoxLayout()
		self.main_layout.addLayout(controls)


		btn_close = QPushButton("close")
		btn_close.clicked.connect(self.close)


		btn_save = QPushButton("save")
		btn_save.clicked.connect(self.save)


		controls.addStretch()
		controls.addWidget(btn_save)
		controls.addWidget(btn_close)



	def save(self):
		data = {
			"text": self.edit_text.text()
		}

		if self.cb:
			self.cb(data)
