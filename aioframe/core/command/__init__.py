import sys
import os
from aioframe.core.command.manuals import console_help, bad_command, bad_object, bad_name
import aioframe.core
from aioframe.core.command.consts import *


class CommandProcess(object):

    def __init__(self):
        self.path = os.getcwd()
        self.path = '/var/www'
        self.argv = sys.argv[1:]

        if len(self.argv) < 3:
            print(console_help)
            return

        self.command, self.object, self.name = self.argv

        if self.command not in COMMAND:
            print(bad_command.format(self.command))
            return

        if self.object not in OBJECT:
            print(bad_object.format(self.object))
            return

        if self.name in os.listdir(self.path):
            print(bad_name.format(self.name))
            return

        obj = getattr(aioframe.core, self.object)(self.name, self.path)
        getattr(obj, self.command)()


def process_command():
    cp = CommandProcess()

