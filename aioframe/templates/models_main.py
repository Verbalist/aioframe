__author__ = 'verbalist'

import os

import aioframe.templates.db_connect

db = aioframe.templates.db_connect.get_db(os.getcwd()+'/config.txt')