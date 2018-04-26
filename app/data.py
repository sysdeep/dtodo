#!/usr/bin/env python3
# -*- coding: utf-8 -*-


TODO_STATUS_NEW = 0
TODO_STATUS_WORK = 1
TODO_STATUS_COMPLETE = 2
TODO_STATUS_CANCEL = 3
TODO_STATUS_ARCHIVE = 4



TODO_STATUSES = {
	TODO_STATUS_NEW			: "Новое",
	TODO_STATUS_WORK		: "В работе",
	TODO_STATUS_COMPLETE	: "Завершено",
	TODO_STATUS_CANCEL		: "Отменено",
	TODO_STATUS_ARCHIVE		: "Архив",
}

TODO_PRIORITYES = {
	0	: "Не важно",
	10	: "Важно",
	20	: "Очень важно",
	30	: "Немедленно",
}