# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re


def get_version():
    """Get the current version of the hotness package"""
    with open("flathub-notifier/__init__.py", "r") as fd:
        regex = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
        version = re.search(regex, fd.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError("No version set in flathub-notifier/__init__.py")
    return version


def get_requirements(requirements_file="requirements.txt"):
    """Get the contents of a file listing the requirements.

    :arg requirements_file: path to a requirements file
    :type requirements_file: string
    :returns: the list of requirements, or an empty list if
              `requirements_file` could not be opened or read
    :return type: list
    """

    lines = open(requirements_file).readlines()
    return [line.rstrip().split("#")[0] for line in lines if not line.startswith("#")]


setup(
    name="flathub-notifier",
    version=get_version(),
    description="Consume anitya fedora messaging messages to file Flathub issues",
    license="LGPLv3",
    author="Zlopez",
    author_email="michal.konecny@packetseekers.eu",
    url="https://github.com/Zlopez/flathub-notifier",
    install_requires=get_requirements(),
    tests_require=get_requirements("dev-requirements.txt"),
    packages=find_packages(exclude=("flathub-notifier.tests", "flathub-notifier.tests.*")),
    test_suite="flathub-notifier.tests",
)
