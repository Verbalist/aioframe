
class BaseModel(object):

    def __init__(self):
        pass


class SelectedModel(object):

    objects = []

    def __init__(self):
        pass


class Driver(object):

    conn = None
    _cursor = None

    def __init__(self, driver):
        self.driver = driver

    def connection(self, dsn):
        self.conn = self.driver.connect(dsn)
        return self.conn

    def cursor(self):
        if self._cursor is not None and not self._cursor.isclose():
            return self._cursor
        return self.conn.cursor()


class Model(object):

    driver = None
    conn = None
    cursor = None

    def __init__(self, driver, dsn):
        self.driver = driver
        self.dsn = dsn

    # def query(self):
    #
    #     self.driver.c

    def check_cursor(self, f):
        if self.conn is None:
            self.conn = self.driver.connection(self.dsn)
        if self.cursor is None or self.cursor.isclose():
            self.cursor = self.driver.cursor()

        return f
