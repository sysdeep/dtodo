#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	QSystemTrayIcon.NoIcon	0	No icon is shown.
	QSystemTrayIcon.Information	1	An information icon is shown.
	QSystemTrayIcon.Warning	2	A standard warning icon is shown.
	QSystemTrayIcon.Critical	3	A critical warning icon is shown.

"""
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal

# from .. import events

class SystemTray(QSystemTrayIcon):
	# ebus = pyqtSignal(str)
	def __init__(self, icon, parent):
		super(SystemTray, self).__init__(icon, parent)


		self.setToolTip("DToDo")

		self.parent = parent
		self.menu 	= QMenu(parent)
		self.setContextMenu(self.menu)
		self.is_messages_support = self.supportsMessages()
		self.delay 	= 5000		# время отображения всплывающего сообщения ms

		#--- статусы иконок
		self.statuses = {
			"normal"	: 0,
			"info" 		: 1,
			"warning" 	: 2,
			"error"		: 3
		}


		#--- act_exit menu
		hide_action = self.menu.addAction("Скрыть")
		# hide_action.setIcon(qficon("system-shutdown-restart-panel.png"))
		hide_action.triggered.connect(self.parent.hide)


		show_action = self.menu.addAction("Отобразить")
		# show_action.setIcon(qficon("system-shutdown-restart-panel.png"))
		show_action.triggered.connect(self.parent.show)


		#--- act_exit menu
		exit_action = self.menu.addAction("Закрыть")
		# exit_action.setIcon(qficon("system-shutdown-restart-panel.png"))
		exit_action.triggered.connect(self.parent.act_exit)



		#--- подписываемся на события системного трея
		# events.on("show_tray_message", self.show_message)


	#
	#
	# def show_message(self, title, text, state="info", delay=0):
	# 	if self.is_messages_support:
	#
	# 		icon_num = self.statuses.get(state, 0)
	# 		if delay == 0:
	# 			delay = self.delay
	#
	# 		self.showMessage(title, text, icon_num, delay)
	#
