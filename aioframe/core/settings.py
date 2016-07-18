import os

class Settings(object):

    def __init__(self):
        self.setting_path = os.environ['AIO_SETTINGS']
