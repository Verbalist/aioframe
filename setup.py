from distutils.core import setup
import shutil
import os, stat
from platform import system

setup(
    name = 'aioframe',
    packages = ['aioframe.bin', 'aioframe.core'],
    version = '1.0.0',
    description = 'easy framework on asyncio',
    author = 'Mehed Dima',
    author_email = 'enshteynn@ukr.net',
    url = 'https://github.com/Verbalist/aioframe',
    download_url = 'https://github.com/Verbalist/aioframe/archive/master.zip',
    keywords = ['asyncio', 'framework', 'web_server', 'async'],
    classifiers= ["Programming Language :: Python 3"],
    long_description='easy framework on asyncio without orm'
)

if system() == 'Linux':
    filename_path = '/usr/local/bin/aioframe'
    shutil.copyfile('aioframe/bin/aioframe.py', '/usr/local/bin/aioframe')
    os.chmod(os.path.join('/usr/local/bin/aioframe'), stat.S_IRWXO)
