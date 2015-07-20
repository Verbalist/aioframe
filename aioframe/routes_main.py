__author__ = 'verbalist'
import asyncio
class url(object):

    def __init__(self, type_query, pattern, func):
        self.type_query = type_query
        self.pattern = pattern
        self.func = func