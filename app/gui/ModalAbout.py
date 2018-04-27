#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QDialog, QPushButton, QHBoxLayout, QVBoxLayout, \
	QGridLayout, QGroupBox, QTabWidget, QWidget, QScrollArea, QFormLayout, QLineEdit, QComboBox, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

from app.rc import VERSION, get_icon, DESCRIPTION, REPO_URL, EMAIL




class ModalAbout(QDialog):
	def __init__(self, parent=None):
		super(ModalAbout, self).__init__(parent)

		self.setFixedHeight(200)
		self.setFixedWidth(300)

		self.setWindowTitle("О программе")


		self.main_layout = QVBoxLayout(self)



		text_name = "<b>DToDo</b> v {}".format(VERSION)
		text_copyright = "Copyright © 2018 {}".format(EMAIL)

		label_name = QLabel(text_name)
		label_description = QLabel(DESCRIPTION)
		label_description.setWordWrap(True)
		label_copy = QLabel(text_copyright)

		label_link = QLabel()
		label_link.setText("<a href='{}'>{}</a>".format(REPO_URL, REPO_URL))
		label_link.setTextInteractionFlags(Qt.TextBrowserInteraction)
		label_link.setOpenExternalLinks(True)

		self.main_layout.addWidget(label_name)
		self.main_layout.addWidget(label_description)
		self.main_layout.addStretch()
		self.main_layout.addWidget(label_link)
		self.main_layout.addWidget(label_copy)



		controls = QHBoxLayout()
		self.main_layout.addLayout(controls)


		btn_close = QPushButton("Закрыть")
		btn_close.setIcon(QIcon(get_icon("delete.png")))
		btn_close.clicked.connect(self.close)


		controls.addStretch()
		controls.addWidget(btn_close)











if __name__ == "__main__":

	import sys
	from PyQt5.QtWidgets import QApplication
	from ..storage.Item import Item


	app = QApplication(sys.argv)


	dialog = ModalAbout()
	dialog.show()


	# view.show()



	sys.exit(app.exec_())