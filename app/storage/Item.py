#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from uuid import uuid4

class Item(object):
	def __init__(self):
		self.id = ""
		self.text = ""
		self.description = ""
		self.status = 0
		self.category = None
		self.priority = 0



	def load(self, item_dict):
		self.id = item_dict.get("text", "")
		self.text = item_dict.get("text", "")
		self.description = item_dict.get("description", "")
		self.status = item_dict.get("status", "")
		self.category = item_dict.get("category", "")
		self.priority = item_dict.get("priority", "")


	def dump(self):
		data_dict = {
			"id"			: self.id,
			"text"			: self.text,
			"description"	: self.description,
			"status"		: self.status,
			"category"		: self.category,
			"priority"		: self.priority
		}

		return data_dict


	def gen_id(self):
		self.id = str(uuid4())