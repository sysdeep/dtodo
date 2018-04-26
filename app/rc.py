#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path

DIR_SELF 	= os.path.dirname(os.path.abspath(__file__))
DIR_BASE	= os.path.dirname(DIR_SELF)
DIR_MEDIA	= os.path.join(DIR_SELF, "media")


DB_NAME		= "dtodo.json"
DB_PATH		= os.path.join(DIR_BASE, DB_NAME)




def get_media(*subpath):
	return os.path.join(DIR_MEDIA, *subpath)

def get_priority_icon(priority_code):
	return get_media("icons_priority", str(priority_code) + ".png")