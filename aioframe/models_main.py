__author__ = 'verbalist'

import asyncio
import os
import aioframe.db_connect
db = aioframe.db_connect.get_db(os.getcwd()+'/config.txt')