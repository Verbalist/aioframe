import json
import os
import shutil

from docker import Client as DC

from aioframe.core.object import BaseObject
from aioframe.core.settings import Settings
from aioframe.core.container import Container


class Project(BaseObject):

    def __init__(self, name, _path):
        self.name = name
        self.path = os.path.join(_path, name)
        os.chdir(_path)
        self.cli = DC(base_url='unix:///var/run/docker.sock')
        self.settings = Settings(self.path)

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

        os.chdir('..')
        os.mkdir('async')
        with open('Dockerfile', 'w') as d:
            d.write("""FROM ubuntu:14.04
RUN sed -i 's/archive.ubuntu.com/ua.archive.ubuntu.com/' /etc/apt/sources.list && \
apt-get update && \
apt-get install -y vim openssh-server screen git && \
update-rc.d ssh defaults && \
echo 'root:password' | chpasswd && \
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN apt-get install -y python3-pip && pip3 install aiohttp
""")
        # print build container

        for x in [line for line in self.cli.build(path=os.getcwd(), tag='async')]:
            print(json.loads(x.decode())['stream'])

        self.settings.add({'project': {
            'name': self.name,
            'path': self.path,
            'image': 'base_dev',
            'ports': (8090, 8090)
        }})
        self.settings.save()
        print('create project with name: %s' % self.name)

    def delete(self):
        self.stop()
        shutil.rmtree(self.settings.source['project']['path'])
        print('remove project with name: %s' % self.name)

    def run(self):
        print('run connection api...')
        print('run database layer...')
        print('run all container...')
        for container_name in self.settings.source:
            if container_name != 'project':
                Container(container_name, os.path.sep.join(
                    self.settings.source[container_name]['path'].split(os.path.sep)[:-1])).run()

    def stop(self):
        for container_name in self.settings.source:
            if container_name != 'project':
                Container(container_name, os.path.sep.join(
                    self.settings.source[container_name]['path'].split(os.path.sep)[:-1])).stop()
        print('stop all container...')
        print('stop database layer...')
        print('stop connection api...')


if __name__ == '__main__':

    p = Project('test', '/var/www')
    try:
        p.create()
        input('press button')
    finally:
        p.delete()
