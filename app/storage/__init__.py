#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Store import Store
# from .loader import load_storage, write_storage


STORE = None



def get_store():
	global STORE
	if STORE is None:
		store = Store()
		STORE = store
		return store

	return STORE