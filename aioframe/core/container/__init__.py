import os
import shutil

import time

from aioframe.core.settings import Settings
from aioframe.core.object import BaseObject
from aioframe.utils import get_free_port
from docker import Client as DC


class Container(BaseObject):

    def __init__(self, name, _path):
        self.name = name
        self.path = os.path.join(_path, name)
        # TODO it is must be choosen
        self.image = 'async'  # [async, sync, other, base_dev]
        os.chdir(_path)

        self.cli = DC(base_url='unix:///var/run/docker.sock')
        self.settings = Settings()

    def create(self):
        # create async or sync container
        # add volume to setting for this name
        self.settings.add({self.name: {'path': self.path,
                                       'template': self.image,
                                       'image': self.image,
                                       'ports': {8090: get_free_port()},
                                       'entry_point': 'python3 {path}/server.py'.format(path='/opt/' + self.name),
                                       }
                           })

        self.settings.save()

        os.mkdir(self.name)
        os.chdir(self.path)
        with open('server.py', 'w') as f:
            with open('/home/verbalist/PycharmProjects/aioframe/server.py') as r:
                f.write(r.read())

        print('create container with name: %s' % self.name)

    def delete(self):
        self.stop()
        self.settings.source.pop(self.name)
        self.settings.save()
        shutil.rmtree(self.settings.source.get(self.name).get('path'))
        print('remove container with name: %s' % self.name)

    def run(self):
        container_settings = self.settings.source.get(self.name)
        container = {'image': self.image,
                     'volumes': ['/opt/' + self.name],
                     'command': container_settings.get('entry_point'),
                     'name': self.name,
                     'ports': [x for x in container_settings.get('ports')],
                     'host_config': self.cli.create_host_config(
                        port_bindings=container_settings.get('ports'),
                        binds={container_settings.get('path'): {
                            'bind': '/opt/' + self.name,
                        }}
                     )}
        _c = self.cli.create_container(**container)

        self.cli.start(container=_c.get('Id'))
        info = self.cli.inspect_container(container=_c.get('Id'))
        container_ip = info['NetworkSettings']['IPAddress']
        print('http://' + container_ip + ':' + str(list(container_settings.get('ports').keys())[0]))
        print('http://localhost:%s' % str(list(container_settings.get('ports').values())[0]))
        self.settings.source[self.name]['container_id'] = _c.get('Id')
        # TODo print warning to log
        self.settings.save()

    def stop(self):
        container_id = self.settings.source.get(self.name).pop('container_id')
        if container_id is not None:
            self.cli.stop(container=container_id)
            self.cli.remove_container(container=container_id)

if __name__ == '__main__':

    c = Container('inner_test', '/var/www/test')
    try:
        c.create()
        c.run()
        input('press button for stop')
        c.stop()
    finally:
        c.delete()
