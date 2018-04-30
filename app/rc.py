#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os.path

VERSION		= "1.0.0"
DESCRIPTION	= """Программа для ведения простого списка дел"""
REPO_URL	= "https://github.com/sysdeep/dtodo"
EMAIL		= "sysdeep@yandex.ru"

DIR_SELF 	= os.path.dirname(os.path.abspath(__file__))
DIR_BASE	= os.path.dirname(DIR_SELF)
DIR_MEDIA	= os.path.join(DIR_SELF, "media")
DIR_FONTS	= os.path.join(DIR_MEDIA, "fonts")


DB_NAME		= "dtodo_db.json"



APP_NAME 	= "dtodo"



def get_media(*subpath):
	return os.path.join(DIR_MEDIA, *subpath)

def get_priority_icon(priority_code):
	return get_media("icons_priority", str(priority_code) + ".png")

def get_status_icon(status_code):
	return get_media("icons_status", str(status_code) + ".png")


def get_icon(full_name):
	return get_media("icons", full_name)


def get_home_path():
	if sys.platform == 'win32':
		return os.path.join(os.environ['APPDATA'], APP_NAME)
	else:
		return os.path.expanduser(os.path.join("~", "." + APP_NAME))


def get_db_path():
	return os.path.join(get_home_path(), DB_NAME)

def get_font_path(*subpath):
	return os.path.join(DIR_FONTS, *subpath)

