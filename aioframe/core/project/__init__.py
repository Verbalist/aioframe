import json
import os
import shutil

import time
from aioframe.core.object import BaseObject
from docker import Client as DC

from aioframe.core.settings import Settings


class Project(BaseObject):

    def __init__(self, name, _path):
        self.name = name
        self.path = os.path.join(_path, name)
        os.chdir(_path)
        self.cli = DC(base_url='unix:///var/run/docker.sock')

    def create(self):
        # create project dir
        os.mkdir(self.name)
        os.chdir(self.name)

        # create docker image
        os.mkdir('docker-containers')
        os.chdir('docker-containers')
        os.mkdir('base_dev')
        os.chdir('base_dev')

        with open('Dockerfile', 'w') as d:
            d.write("""FROM ubuntu:14.04
RUN sed -i 's/archive.ubuntu.com/ua.archive.ubuntu.com/' /etc/apt/sources.list && \
apt-get update && \
apt-get install -y vim openssh-server screen git && \
update-rc.d ssh defaults && \
echo 'root:password' | chpasswd && \
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
""")
        # print build container

        for x in [line for line in self.cli.build(path=os.getcwd(), tag='base_dev')]:
            print(json.loads(x.decode())['stream'])

        s = Settings(self.path)
        s.add({'project': {
            'name': self.name,
            'path': self.path,
            'image': 'base_dev'
        }})
        s.save()
        print('create project with name: %s' % self.name)

    def delete(self):
        shutil.rmtree(self.path)
        print('remove project with name: %s' % self.name)

    def run(self):
        print('run connection api...')
        print('run database layer...')
        print('run all container...')
        s = Settings()
        for container_name in s.source:
            if container_name != 'project':
                print('run container %s' % container_name)
                c = s.get(container_name)
                _c = self.cli.create_container(c.get('image'), volumes=[c.get('path')],
                                               command='python3 {path}/server.py'.format(path=c.get('path')))
                self.cli.start(container=_c.get('Id'))
                print('it`s works')
                time.sleep(3)
                self.cli.stop(container=_c.get('Id'))
                print('it`s stop')

if __name__ == '__main__':

    p = Project('test', '/var/www')
    try:
        p.create()
        input('press button')
    finally:
        p.delete()
