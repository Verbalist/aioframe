#!/usr/bin/python3
from aioframe.core.command import process_command
import sys

if __name__ == '__main__':
    process_command(sys.argv[1:])