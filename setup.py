from distutils.core import setup

# noinspection PyUnresolvedReferences
import setuptools

setup(
    name='steamtags',
    packages=['steamtags'],
    install_requires=[
    ],
    version='0.1.0',
    description='Steam Tags on PyPI',
    long_description='Steam Tags: an API to match Steam tags with appIDs, written in Python 3.',
    long_description_content_type='text/x-rst',
    author='Wok',
    author_email='wok@tuta.io',
    url='https://github.com/woctezuma/match-steam-tags',
    download_url='https://github.com/woctezuma/match-steam-tags/archive/0.1.0.tar.gz',
    keywords=['steam', 'steamtags', 'tags', 'api'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
