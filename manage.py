__author__ = 'verbalist'

import sys
import creater
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('command', help='foo help')
parser.add_argument('--create_rest', help='create rest files for name')
parser.add_argument('--init', action="store_true", help='create base folder')
parser.add_argument('--default', action="store_true", help='flag to uses default files')
parser.add_argument('--remove', help='delete names folder')


args = parser.parse_args()

if args.create_rest:
    try:
        creater.create_rest(args.create_rest, args.default)
    except FileNotFoundError:
        creater.init()
        creater.create_rest(args.create_rest, args.default)

if args.init:
    creater.init()

if args.remove:
    creater.remove(args.remove)

# if args.default:
#     creater.default()