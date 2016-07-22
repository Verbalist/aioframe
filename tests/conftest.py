import pytest
import time
from docker import Client as DockerClient


@pytest.yield_fixture(scope='session')
def docker():
    cli = DockerClient(base_url='unix:///var/run/docker.sock')
    container = cli.create_container(image='test_db_aioframe')
    container_id = container.get('Id')
    cli.start(container=container_id)
    info = cli.inspect_container(container=container_id)
    container_ip = info['NetworkSettings']['IPAddress']
    time.sleep(1)  # wait docker container restart postgresql
    print('docker start')

    yield container_ip

    cli.stop(container=container_id)
    print('docker stop')
