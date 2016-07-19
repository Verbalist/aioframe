import unittest

class CoreTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(cls.__name__)
