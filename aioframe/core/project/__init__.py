import json
import os
import shutil

import yaml
from aioframe.core.object import BaseObject
from docker import Client as DC


class Project(BaseObject):

    def __init__(self, name, _path):
        self.name = name
        self.path = _path
        os.chdir(_path)
        self.cli = DC(base_url='unix:///var/run/docker.sock')

        # container = cli.create_container(image='test_db_aioframe')
        # container_id = container.get('Id')
        # cli.start(container=container_id)
        # info = cli.inspect_container(container=container_id)
        # container_ip = info['NetworkSettings']['IPAddress']
        # time.sleep(2)  # wait docker container restart postgresql
        # print('docker start')
        # print(_path)

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

        # create setting
        yaml.dump({'project': {
            'name': self.name,
            'path': self.path,
            'image': 'base_dev'
        }})

        print('create project with name: %s' % self.name)

    def delete(self):
        shutil.rmtree(os.path.join(self.path, self.name))
        print('remove project with name: %s' % self.name)

    def run(self):
        pass


if __name__ == '__main__':
    # cli = DC(base_url='unix:///var/run/docker.sock')
    # c_1 = cli.create_container(image='test_db_aioframe')
    # cli.start(container=c_1.get('Id'))
    # info = cli.inspect_container(container=c_1.get('Id'))
    # print(info['NetworkSettings']['IPAddress'])
    # c_2 = cli.create_container(image='test_db_aioframe')
    # cli.start(container=c_2.get('Id'))
    # info = cli.inspect_container(container=c_2.get('Id'))
    # print(info['NetworkSettings']['IPAddress'])
    #
    # cli.stop(container=c_1.get('ID'))
    # cli.stop(container=c_2.get('ID'))

    p = Project('test', '/var/www')
    try:
        p.create()
        input('press button')
    finally:
        p.delete()
