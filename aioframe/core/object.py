import abc


class BaseObject(metaclass=abc.ABCMeta):
    name = None

    @abc.abstractmethod
    def create(self):
        pass

    @abc.abstractmethod
    def delete(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass
