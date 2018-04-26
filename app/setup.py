#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path

from .rc import get_home_path





def check_home():

	home_path = get_home_path()

	if not os.path.exists(home_path):
		os.makedirs(home_path, exist_ok=True)
