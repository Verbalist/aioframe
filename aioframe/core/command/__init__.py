import sys
import os
from aioframe.core.command.manuals import console_help
import aioframe.core

COMMAND = ('create', 'remove')
OBJECT = ('project', 'container', 'block', 'microservice')


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
            message = """failed command: %s\n\nAVAILABLE COMMANDS:\n\t%s""" % (self.command, '\n\t'.join(COMMAND))
            print(message)
            return

        if self.object not in OBJECT:
            message = """failed object: %s\n\nAVAILABLE OBJECTS:\n\t%s""" % (self.object, '\n\t'.join(OBJECT))
            print(message)
            return

        if self.name in os.listdir(self.path):
            print('failed name: %s\nThis name is not available' % self.name)
            return

        obj = getattr(aioframe.core, self.object)(self.name)
        getattr(obj, self.command)()


def process_command():
    cp = CommandProcess()

if __name__ == '__main__':
    sys.argv = ('/aioframe', 'create', 'project', 'test')
    process_command()

    sys.argv = ('/aioframe', 'remove', 'project', 'test')
    process_command()

    sys.argv = ('/aioframe', 'rmove', 'project', 'test')
    process_command()

    sys.argv = ('/aioframe', 'remove', 'prject', 'test')
    process_command()

    with open('/var/www/test_exist', 'w') as f:
        f.write('test_exist')
    sys.argv = ('/aioframe', 'remove', 'project', 'test_exist')
    process_command()

