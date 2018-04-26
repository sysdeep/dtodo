#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
from .Item import Item
from . import loader

class Store(object):
	def __init__(self):
		self.db_path = ""
		self.items = []





	def add_item(self, data_dict):
		for key, value in data_dict.items():
			item = Item()
			item.gen_id()
			if hasattr(item, key):
				setattr(item, key, value)

			self.items.append(item)





	def open(self, db_path):
		self.db_path = db_path

		if not os.path.exists(db_path):
			self.save()
			return False


		data_dict = loader.read_db(self.db_path)
		self.load(data_dict)


	def save(self):
		data_dict = self.dump()
		loader.write_db(self.db_path, data_dict)




	def load(self, data_dict):
		items = data_dict.get("items")
		if items is None:
			return False

		for item in items:
			titem = Item()
			titem.load(item)
			self.items.append(titem)





	def dump(self):
		data_dict = {
			"items"	: []
		}

		for item in self.items:
			data_dict["items"].append(item.dump())

		return data_dict