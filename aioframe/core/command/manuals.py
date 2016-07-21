from aioframe.core.command.consts import *

console_help = """
[help]
[command]
    create
        project
        container
        block
        microservice
            $name

    delete
        project
        container
        block
        microservice
            $name
"""

bad_command = """failed command: {}\n\nAVAILABLE COMMANDS:\n\t%s""" % '\n\t'.join(COMMAND)
bad_object = """failed object: {}\n\nAVAILABLE OBJECTS:\n\t%s""" % '\n\t'.join(OBJECT)
bad_name = 'failed name: {}\nThis name is not available'
