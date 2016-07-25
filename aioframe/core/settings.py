import os
from aioframe.utils.yaml_utils import *
from aioframe.utils import Singleton
from aioframe.exceptions import CommandException


@Singleton
class Settings(object):

    source = OrderedDict()

    def __init__(self, _path=None):
        if _path is None:
            self.path = self.search_settings()
            try:
                self.source = OrderedDict(yaml.load(open(os.path.join(self.path, 'settings.yaml'))))
            except FileNotFoundError:
                raise CommandException('Create project first')
        else:
            self.path = _path

    def add(self, value, tag=None):
        if tag is None:
            self.source.update(value)
        else:
            self.source[tag] = value

    @staticmethod
    def search_settings():
        p = os.getcwd().split(os.path.sep)
        while len(p) > 1:
            if 'settings.yaml' in os.listdir(os.path.sep.join(p)):
                break
            else:
                p = p[:-1]

        return os.path.sep.join(p)

    def get(self, key):
        return self.source.get(key)

    def save(self):
        self.source.move_to_end('project', last=False)
        yaml.dump(self.source, stream=open(os.path.join(self.path, 'settings.yaml'), 'w'), default_flow_style=False)

    # def __del__(self):
    #     self.save()
