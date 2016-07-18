__author__ = 'verbalist'

import os
import shutil

import traceback

templates = ('controllers', 'views', 'models', 'routes')


def init(project_name):
    project_path = os.path.join(os.getcwd(), project_name)
    try:
        os.mkdir(project_path)
        os.chdir(project_path)
        for names in templates:
            os.mkdir(names)
            shutil.copyfile(os.path.join(os.getcwd(), 'aioframe', '%s_main.py' % names),
                            os.path.join(project_path, '%s/main.py' % names))
    except Exception as e:
        for tb in traceback.format_tb(e.__traceback__):
            print(tb, e)

        os.chdir('..')
        shutil.rmtree(project_path)
    return project_path
