# -*- coding: utf-8 -*-
# tgmysqldb.py
# Copyright (C) 2017-2020 KunoiSayami
#
# This module is part of WelcomeBot-Telegram and is released under
# the AGPL v3 License: https://www.gnu.org/licenses/agpl-3.0.txt
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
from libpy3.mysqldb import mysqldb as MDB

class mysqldb(MDB):
	def insert_last_message_id(self, chat_id: int, message_id: int):
		self.execute("UPDATE `welcomemsg` SET `previous_msg` = %s WHERE `group_id` = %s", (message_id, chat_id))

	def query_last_message_id(self, chat_id: int) -> int:
		return self.query1("SELECT `previous_msg` FROM `welcomemsg` WHERE `group_id` = %s", chat_id)['previous_msg']
