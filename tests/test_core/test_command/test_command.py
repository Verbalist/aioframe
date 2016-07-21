import logging
import os
import subprocess

from aioframe.core.command.manuals import console_help, bad_command, bad_object, bad_name
a = logging.getLogger()


class TestCommandProcess(object):

    def setup_method(self, f):
        os.chdir('/var/www')

    def test_process_command_help(self):
        _help = subprocess.check_output(['aioframe'], shell=True)
        assert _help == console_help.encode() + b'\n'

    def test_process_command_help_bad_command(self):
        _help = subprocess.check_output(['aioframe a a a'], shell=True)
        assert _help == bad_command.format('a').encode() + b'\n'

    def test_process_command_bad_object(self):
        _help = subprocess.check_output(['aioframe create a a'], shell=True)
        assert _help == bad_object.format('a').encode() + b'\n'

    def test_process_command_exist_name(self):
        with open('test_exist', 'w') as f:
            f.write('test_exist')
        _help = subprocess.check_output(['aioframe create project test_exist'], shell=True)
        assert _help == bad_name.format('test_exist').encode() + b'\n'
        os.remove('test_exist')

    def test_process_command_create_project(self):
        _help = subprocess.check_output(['aioframe create project test'], shell=True)
        assert _help == b'create project with name: test\n'
