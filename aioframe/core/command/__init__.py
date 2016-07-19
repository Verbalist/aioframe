import sys
import os


class CommandProcess(object):

    def __init__(self):
        self.path = os.getcwd()
        print(self.path)
        print(sys.argv)

    def run(self):
        pass


def process_command():
    cp = CommandProcess()
    cp.run()
