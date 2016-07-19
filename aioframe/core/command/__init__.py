import sys
import os
from aioframe.core.command.manuals import console_help


class CommandProcess(object):

    def __init__(self):
        # self.path = os.getcwd()
        self.path = '/var/www'
        self.argv = sys.argv[1:]
        print(self.argv)
        if not self.argv:
            print(console_help)
            return


def process_command():
    cp = CommandProcess()

if __name__ == '__main__':
    sys.argv = ('/aioframe', 'create', 'project', 'test')
    sys.argv = ('./aioframe',)
    process_command()
