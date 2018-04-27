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
		print("add item")
		item = Item()
		for key, value in data_dict.items():
			if hasattr(item, key):
				setattr(item, key, value)

		item.gen_id()
		item.create_timestamps()
		self.items.append(item)


	def update_item(self, data_dict):
		tid = data_dict.get("id")
		if tid is None:
			print("Error: update_item - no id in request")
			return False

		item = self.find_id(tid)
		# print(item.text)
		for key, value in data_dict.items():
			if hasattr(item, key):
				setattr(item, key, value)

		item.update_timestamps()


	def remove_item(self, item_id):
		print("remove item: " + item_id)
		item = self.find_id(item_id)
		self.items.remove(item)



	def find_id(self, id):
		result = [item for item in self.items if item.id == id]
		return result[0] if len(result) > 0 else Item()










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