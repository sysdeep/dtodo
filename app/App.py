#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	App - класс обёртка для сокрытия деталей

	app = App()
	app.start()





	2017.10.04 - переход на pyqt 5.9 -> в консоли вываливается "QApplication: invalid style override passed, ignoring it."
	Ваше окружение линукс с GTK3 или что-то еще экзотичное? Qt ругается на стиль темы, полученной от окружения.
	Можно попробовать вызвать статический метод ДО создания QApplication (они определены как classmethod в PyQt?)

		QApplication.setDesktopSettingsAware(False)

	В С++ можно было выдать каков стиль задается программе на отладку, но я не знаю как это записать на питоне.

	qDebug() << QApplication::style()->metaObject()->className();
"""
import signal
import sys
import logging

from PyQt5.QtWidgets import QApplication

from .gui.MainWindow import MainWindow
from .storage import get_store
from .rc import DB_PATH


log = logging.getLogger("main")

class App(object):
	"""
		обёртка над всем добром
	"""
	def __init__(self):
		log.info("инициализация приложения")


		store = get_store()
		store.open(DB_PATH)


		# write_storage(DB_PATH)
		# load_storage(DB_PATH)

		# QApplication.setDesktopSettingsAware(False)


		#--- наше приложение
		self.qtapp = QApplication(sys.argv)						#: qqq
		self.main_window = MainWindow()

		# print(QApplication.style().metaObject().className())		# тек. стиль

		#--- перехват системных сигналов
		signal.signal(signal.SIGINT, self.__signal_handler)		# обработка Ctrl+C


	def __signal_handler(self, signum, frame):
		"""обработчик сигнала завершения от системы"""
		log.info("перехвачен сигнал SIGINT(Ctrl+C)")
		log.info("запрос на выход из cmd")
		self.qtapp.exit(0)
		log.info("приложение GUI - остановленно")
		sys.exit(0)



	def start(self):
		"""запуск приложения"""
		log.info("запуск приложения")

		# self.main_window = MainWindow()
		self.qtapp.exec_()

		log.info("приложение остановленно")
		sys.exit(0)







