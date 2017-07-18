import sys, os
from setuptools import setup, find_packages
import subprocess

NAME = "fbiter"
HERE = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(HERE, NAME, '_version.py')) as f:
    exec(f.read(), {}, version_ns)

with open(os.path.join(HERE, 'requirements.txt')) as f:
    requirements = f.read().strip().split("\n")

setup(
    name = NAME,
    description = "A simple library for iterating through paginated Facebook API endpoints.",
    version = version_ns['__version__'],
    packages = find_packages(exclude=["test",]),
    tests_require = [ "nose", ] + requirements,
    install_requires = requirements,
    author = "Jeremy Singer-Vine",
    author_email = "jsvine@gmail.com",
    license = "MIT",
    keywords = "facebook api",
    url = "https://github.com/jsvine/fbiter",
)
