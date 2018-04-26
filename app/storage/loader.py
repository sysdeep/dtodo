#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def read_db(db_path):

	with open(db_path, "r", encoding="utf-8") as fd:
		jdata = fd.read()
		data = json.loads(jdata)

		return data


def write_db(db_path, data):

	with open(db_path, "w", encoding="utf-8") as fd:
		jdata = json.dumps(data, ensure_ascii=False, indent=4)
		fd.write(jdata)

