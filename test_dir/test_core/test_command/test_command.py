import sys
from core.command import process_command
from test_dir.test_core.main import CoreTest

class CommandProcessTest(CoreTest):

    def test_process_command_help(self):
        sys.argv = ('./aioframe',)
        process_command()

