from setuptools import find_packages, setup
version = __import__('aioframe').__version__

setup(
    name='aioframe',
    packages=find_packages(),
    # packages=find_packages(exclude=['aioframe.bin']),  # 'aioframe.core.command'
    include_package_data=True,
    # scripts={'aioframe/bin/aioframe.py'},
    entry_points={'console_scripts': [
        'aioframe=aioframe.core.command:process_command',
    ]},
    version=version,
    description='easy framework on asyncio',
    author='Mekhed Dima',
    author_email='enshteynn@ukr.net',
    url='https://github.com/Verbalist/aioframe',
    download_url='https://github.com/Verbalist/aioframe/archive/master.zip',
    keywords=['asyncio', 'framework', 'web_server', 'async'],
    classifiers=["Programming Language :: Python 3"],
    long_description='easy framework on asyncio without orm'
)

# if system() == 'Linux':
#     filename_path = '/usr/local/bin/aioframe'
#     shutil.copyfile('aioframe/bin/aioframe.py', '/usr/local/bin/aioframe')
#     os.chmod(os.path.join('/usr/local/bin/aioframe'), stat.S_IRWXO)
