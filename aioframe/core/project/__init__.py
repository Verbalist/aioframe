from aioframe.core.object import BaseObject


class Project(BaseObject):

    def __init__(self, name):
        self.name = name

    def create(self):
        print('create project with name: %s' % self.name)

    def remove(self):
        print('remove project with name: %s' % self.name)
