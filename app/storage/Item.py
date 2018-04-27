#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from uuid import uuid4

class Item(object):
	def __init__(self):
		self.id = ""
		self.text = ""
		self.description = ""
		self.status = 0
		self.category = None
		self.priority = 0
		self.created = 0
		self.updated = 0



	def load(self, item_dict):
		ntime = time.time()
		self.id = item_dict.get("id", "")
		self.text = item_dict.get("text", "")
		self.description = item_dict.get("description", "")
		self.status = item_dict.get("status", "")
		self.category = item_dict.get("category", "")
		self.priority = item_dict.get("priority", "")
		self.created = item_dict.get("created", ntime)
		self.updated = item_dict.get("updated", ntime)


	def dump(self):
		data_dict = {
			"id"			: self.id,
			"text"			: self.text,
			"description"	: self.description,
			"status"		: self.status,
			"category"		: self.category,
			"priority"		: self.priority,
			"created"		: self.created,
			"updated"		: self.updated
		}

		return data_dict


	def gen_id(self):
		self.id = str(uuid4())


	@staticmethod
	def fdate(seconds):
		ltime = time.localtime(seconds)
		return time.strftime("%Y-%m-%d %H:%M:%S", ltime)


	def create_timestamps(self):
		self.created = time.time()
		self.updated = time.time()

	def update_timestamps(self):
		self.updated = time.time()