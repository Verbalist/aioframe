import os
import time
from aioframe.core.object import BaseObject
from docker import Client as DC


class Container(BaseObject):

    def __init__(self, name, _path):
        self.name = name
        self.path = _path
        os.chdir(_path)

        cli = DC(base_url='unix:///var/run/docker.sock')
        os.mkdir(self.name)
        os.chdir(self.name)

        # create async or sync container
        # add volume to setting for this name

        container = cli.create_container(image='test_db_aioframe')
        container_id = container.get('Id')
        cli.start(container=container_id)
        info = cli.inspect_container(container=container_id)
        container_ip = info['NetworkSettings']['IPAddress']
        time.sleep(2)  # wait docker container restart postgresql
        print('docker start')
        print(_path)

    def create(self):
        print('create container with name: %s' % self.name)

    def delete(self):
        print('remove container with name: %s' % self.name)

    def run(self):
        pass