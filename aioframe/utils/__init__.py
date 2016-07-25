class Singleton(object):

    def __init__(self, _class):
        self._class = _class
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self._class(*args, **kwargs)
        return self.instance
