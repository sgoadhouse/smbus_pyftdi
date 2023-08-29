# The MIT License (MIT)
# Copyright (c) 2017 Karl-Petter Lindegaard

import re
import os
from io import open
from setuptools import setup


def read_file(fname, encoding='utf-8'):
    with open(fname, encoding=encoding) as r:
        return r.read()


def find_version(*file_paths):
    fpath = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = read_file(fpath)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)

    err_msg = 'Unable to find version string in {}'.format(fpath)
    raise RuntimeError(err_msg)


README = read_file('README.md')
version = find_version('smbus_pyftdi', '__init__.py')
test_deps = [
    'mock;python_version<"3.3"',
    'nose'
]

setup(
    name="smbus_pyftdi",
    version=version,
    author="Stephen Goadhouse",
    author_email="sgoadhouse@gmail.com",
    description="smbus_pyftdi is a SMBUS python Library that uses pyFTDI for the low-level I2C transactions and uses the same API as the Python package smbus and smbus2",
    license="MIT",
    keywords=['smbus', 'pyftdi', 'ftdi', 'python', 'i2c', 'pmbus'],
    url="https://github.com/sgoadhouse/smbus_pyftdi",
    packages=['smbus_pyftdi'],
    package_data={'smbus_pyftdi': ['py.typed', 'smbus_pyftdi.pyi']},
    long_description=README,
    long_description_content_type="text/markdown",
    extras_require={
        'docs': [
            'sphinx >= 1.5.3'
        ],
        'qa': [
            'flake8'
        ],
        'test': test_deps
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ],
)
