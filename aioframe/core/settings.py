import os
from aioframe.utils.yaml_utils import *
from aioframe.utils import Singleton
from aioframe.exceptions import CommandException


@Singleton
class Settings(object):

    source = OrderedDict()

    def __init__(self, _path=None):
        self.path = self.search_settings()
        try:
            self.source = OrderedDict(yaml.load(open(os.path.join(self.path, 'settings.yaml'))))
        except FileNotFoundError:
                raise CommandException('Create project first')

    def add(self, value, tag=None):
        if tag is None:
            self.source.update(value)
        else:
            self.source[tag] = value

    @staticmethod
    def search_settings():
        p = os.getcwd().split(os.path.sep)
        while len(p) > 1:
            try:
                if 'settings.yaml' in os.listdir(os.path.sep.join(p)):
                    break
                else:
                    p = p[:-1]
            except FileNotFoundError:
                p = p[:-1]

        return os.path.sep.join(p)

    def save(self):
        self.source.move_to_end('project', last=False)
        yaml.dump(self.source, stream=open(os.path.join(self.path, 'settings.yaml'), 'w'), default_flow_style=False)

    def get(self, item):
        return self.source.get(item)
