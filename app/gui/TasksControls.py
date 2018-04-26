#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal

class TaskControls(QWidget):

	eadd = pyqtSignal()

	def __init__(self, parent=None):
		super(TaskControls, self).__init__(parent)

		self.main_layout = QVBoxLayout(self)
		self.list = QListWidget()

		self.main_layout.addWidget(self.list)


		item = QListWidgetItem("controls")
		self.list.addItem(item)


		controls = QHBoxLayout()
		self.main_layout.addLayout(controls)


		btn_add = QPushButton("Add")
		btn_add.clicked.connect(self.show_add_item)

		controls.addWidget(btn_add)




	def show_add_item(self):
		self.eadd.emit()