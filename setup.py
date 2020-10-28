import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='steamtags',
    version='0.1.2',
    author='Wok',
    author_email='wok@tuta.io',
    description='Steam Tags on PyPI',
    keywords=['steam', 'steamtags', 'tags', 'api'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/woctezuma/match-steam-tags',
    download_url='https://github.com/woctezuma/match-steam-tags/archive/0.1.2.tar.gz',
    packages=setuptools.find_packages(),
    install_requires=[
        'gamedatacrunch',
        'steamspypi',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Games/Entertainment',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
