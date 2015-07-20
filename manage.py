__author__ = 'verbalist'

from aioframe.creater import *
import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--create_rest', help='create rest files for name')
parser.add_argument('--init', action="store_true", help='create base folder')
parser.add_argument('--default', action="store_true", help='flag to uses default files')
parser.add_argument('--remove', help='delete names folder')


args = parser.parse_args()

if args.create_rest:
    try:
        create_rest(args.create_rest, os.getcwd() + '/', args.default)
    except FileNotFoundError:
        init(os.getcwd() + '/')
        create_rest(args.create_rest, os.getcwd() + '/', args.default)

if args.init:
    init(os.getcwd() + '/')

if args.remove:
    remove(args.remove, os.getcwd() + '/')

# if args.default:
#     creater.default()