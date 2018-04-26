#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from app.App import App
app = App()
app.start()


#
#
# def main():
# 	#--- парсер командной строки
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument("-c", "--command", help="команда", choices=["get_project", "project_editor"])
# 	parser.add_argument("-s", "--server", help="сервер")
# 	parser.add_argument("-p", "--port", help="порт")
# 	args = parser.parse_args()
#
#
# 	if args.command == "get_project":
# 		return get_project_json(HTTP_PROJECT_GET, FILE_PROJECT)
#
# 	if args.command == "project_editor":
# 		return start_project_editor()
#
# 	from app.config import config
#
# 	if args.server:
# 		config.set("main", "server_host", args.server)
#
# 	if args.port:
# 		config.set("main", "server_port", args.port)
#
# 	start_app()
#
#
# main()
