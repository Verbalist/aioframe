import os
import shutil

import time

from aioframe.core.settings import Settings
from aioframe.core.object import BaseObject
from docker import Client as DC


class Container(BaseObject):

    def __init__(self, name, _path):
        self.name = name
        self.path = os.path.join(_path, name)
        self.image = 'base_dev'  # [async, sync, other, base_dev]
        os.chdir(_path)

        self.cli = DC(base_url='unix:///var/run/docker.sock')

        # create async or sync container
        # add volume to setting for this name
        settings = Settings()
        settings.add({self.name: {'path': self.path,
                                  'template': self.image,
                                  'image': 'base_dev'}})
        settings.save()

    def create(self):
        os.mkdir(self.name)
        os.chdir(self.path)
        with open('server.py', 'w') as f:
            f.write('print(\'run server %s\')' % self.name)

        print('create container with name: %s' % self.name)

    def delete(self):
        shutil.rmtree(self.path)
        print('remove container with name: %s' % self.name)

    def run(self):
        print('run container %s' % self.name)
        _c = self.cli.create_container(self.image, volumes=[self.path],
                                       command='python3 {path}/server.py'.format(path=self.path))
        self.cli.start(container=_c.get('Id'))
        print('it`s works')
        time.sleep(3)
        self.cli.stop(container=_c.get('Id'))
        print('it`s stop')

if __name__ == '__main__':

    c = Container('inner_test', '/var/www/test')
    try:
        c.create()
        c.run()
        input('press button')
    finally:
        c.delete()
