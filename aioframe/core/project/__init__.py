import os
import shutil
from aioframe.core.object import BaseObject


class Project(BaseObject):

    def __init__(self, name, _path):
        self.name = name

        # create connection API

        # create DAO

        # create applications module

        # old rest MVC
        # modules = ('views', 'models', 'routes', 'controllers')
        # for m in modules:
        #     os.mkdir(m)
        #     shutil.copyfile('aioframe/templates/%s_main.py', os.path.join(_path, m, 'main.py'))

    def create(self):
        print('create project with name: %s' % self.name)


    def remove(self):
        print('remove project with name: %s' % self.name)
