import abc
import os
import random
import time
import traceback
from collections import Iterable
import inspect


class BaseModel(object):

    def __init__(self):
        pass


class RawQueryModel(object):

    objects = []

    def __init__(self):
        pass


class BaseCursor(metaclass=abc.ABCMeta):
    closed = 1

    @abc.abstractmethod
    def execute(self, query_string, args):
        pass

    @abc.abstractmethod
    def fetchone(self):
        pass

    @abc.abstractmethod
    def fetchall(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass


class DictCursor(BaseCursor):

    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, query_string, args):
        self.cursor.execute(query_string, args)

    def fetchone(self):
        pass

    def fetchall(self):
        res = self.cursor.fetchall()
        if res is None:
            return res

        if len(res) == 1:
            return {self.cursor.description[i].name: col for i, col in enumerate(res[0])}
        else:
            return [{self.cursor.description[i].name: col for i, col in enumerate(row)} for row in res]

    def close(self):
        self.cursor.close()


class ObjectCursor(BaseCursor):

    class Entity(object):

        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, query_string, args):
        self.cursor.execute(query_string, args)

    def fetchone(self):
        pass

    def fetchall(self, name=None):
        res = self.cursor.fetchall()
        if res is None:
            return res

        if len(res) == 1:
            if name is None:
                name = 'new' + str(random.randint(0, 15))
                _class = type(name, (self.Entity,), {col.name: None for col in self.cursor.description})
            else:
                # наркомания с созданием модели
                _class = type(name, (self.Entity,), {col.name: None for col in self.cursor.description})
                path = '/'.join(inspect.stack()[3][1].split('/')[:-1])
                if 'models.py' not in os.listdir(path):
                    with open(os.path.join(path, 'models.py'), 'w') as f:
                        f.write('from aioframe.models import RawQueryModel\n')

                with open(os.path.join(path, 'models.py'), 'r') as r:
                    if r.read().find('class %s' % name) == -1:
                        with open(os.path.join(path, 'models.py'), 'a') as f:
                            f.write("""\n\nclass {name}(RawQueryModel):\n\n    {attrs}\n""".format(name=name,
                                attrs='\n    '.join([col.name + ' = ' + str(col.type_code)
                                                     for col in self.cursor.description])))
                 # конец наркомании
            return _class(**{self.cursor.description[i].name: col for i, col in enumerate(res[0])})
        else:
            _class = type(name, (self.Entity,), {col.name: None for col in self.cursor.description})
            return [_class(**{self.cursor.description[i].name: col for i, col in enumerate(row)}) for row in res]

    def close(self):
        self.cursor.close()


class Driver(object):

    conn = None
    _cursor = None

    def __init__(self, driver):
        self.driver = driver

    def connection(self, dsn):
        if type(dsn) == str:
            self.conn = self.driver.connect(dsn)
        else:
            self.conn = self.driver.connect(**dsn)
        return self.conn

    def cursor(self):
        if self._cursor is not None and not self._cursor.closed:
            return self._cursor
        return ObjectCursor(self.conn.cursor())

    @staticmethod
    def check_cursor(f):
        def wrapper(self, *args, **kwargs):
            if self.conn is None:
                self.conn = self.driver.connection(self.dsn)

            if self.cursor is None or self.cursor.closed:
                self.cursor = self.driver.cursor()
            return f(self, *args, **kwargs)

        return wrapper


class Model(object):

    driver = Driver(None)
    conn = None
    cursor = None

    def __init__(self, driver, dsn):
        self.driver.driver = driver
        self.dsn = dsn

    @Driver.check_cursor
    def query(self, query_string, args=(), name=None):
        if not isinstance(args, Iterable):
            args = (args, )
        self.cursor.execute(query_string, args)
        return self.cursor.fetchall(name)

    @Driver.check_cursor
    def execute(self, query_string, args=()):
        if not isinstance(args, Iterable):
            args = (args, )
        try:
            self.cursor.execute(query_string, args)
        except Exception as e:
            return e

if __name__ == '__main__':
    # docker stop $(docker ps -a -q)
    from docker import Client as DockerClient

    cli = DockerClient(base_url='unix:///var/run/docker.sock')
    try:
        container = cli.create_container(image='test_db_aioframe')
        container_id = container.get('Id')
        cli.start(container=container_id)
        info = cli.inspect_container(container=container_id)
        container_ip = info['NetworkSettings']['IPAddress']
        time.sleep(1)  # wait docker container restart postgresql
        print('docker start')

        import psycopg2
        d = Model(psycopg2, {'database': 'test', 'user': 'test', 'host': container_ip, 'password': 'test'})
        _c = d.query('select %s as vasa, %s as petya', (1, 1), name='A1')

    except Exception as e:
        for x in traceback.format_tb(e.__traceback__): print(x)
    finally:
        cli.close()
        print('docker stop')
