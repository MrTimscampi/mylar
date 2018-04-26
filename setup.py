from setuptools_scm import get_version
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mylar',
    version=get_version(),

    description='An automated Comic Book downloader (cbr/cbz) for use with SABnzbd, NZBGet and torrents ',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/evilhero/mylar',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: System Administrators',
        'Topic :: Home Automation',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='comic torrent newsgroup automation',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'apscheduler',
        'cherrypy',
        'requests',
        'feedparser',
        'cfscrape',
        'bs4',
        'deluge_client',
        'python-qbittorrent',
        'simplejson',
        'mako',
        'portend',
        'bencode-python3',
        'transmissionrpc'
    ],

    extras_require={
        'dev': [],
        'test': [],
    },

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'mylar=mylar.Mylar:main',
        ],
    },
)