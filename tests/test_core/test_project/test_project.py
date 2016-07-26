import os

from aioframe.core.project import Project
from aioframe.core.container import Container


def test_container():
    p = Project('test', '/var/www')
    p.create()
    os.chdir('/var/www/test')
    c = Container('test1', '/var/www/test')
    c.create()
    c.run()
    p.run()
    p.stop()
    c.delete()
    p.delete()
