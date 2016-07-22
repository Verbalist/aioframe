from setuptools import find_packages, setup
version = __import__('aioframe').__version__

setup(
    name='aioframe',
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['aioframe=aioframe.core.command:process_command']},
    version=version,
    description='easy framework on asyncio',
    author='Mekhed Dima',
    author_email='enshteynn@ukr.net',
    url='https://github.com/Verbalist/aioframe',
    download_url='https://github.com/Verbalist/aioframe/archive/master.zip',
    keywords=['asyncio', 'framework', 'web_server', 'async'],
    classifiers=["Programming Language :: Python 3"],
    long_description='easy framework on asyncio without orm', requires=['docker-py']
)
