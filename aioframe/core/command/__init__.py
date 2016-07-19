import sys
import os
from core.command.manuals import console_help
import core


class CommandProcess(object):

    def __init__(self):
        self.path = os.getcwd()
        self.path = '/var/www'
        self.argv = sys.argv[1:]

        if len(self.argv) < 3:
            print(console_help)
            return

        self.action, self.object, self.name = self.argv
        obj = getattr(core, self.object)(self.name)
        getattr(obj, self.action)()




def process_command():
    cp = CommandProcess()

if __name__ == '__main__':
    sys.argv = ('/aioframe', 'create', 'project', 'test')
    process_command()

    sys.argv = ('/aioframe', 'remove', 'project', 'test')
    process_command()