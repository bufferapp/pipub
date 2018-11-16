# !/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="pipub",
    packages=find_packages(),
    version="0.1.1",
    description="Pipe data from the command line to Google Pubsub.",
    author="David Gasquez",
    license="MIT",
    author_email="davidgasquez@buffer.com",
    url="https://github.com/bufferapp/pipub",
    keywords=["pubsub", "pipe", "stream", "google"],
    install_requires=["google-cloud-pubsub", "click"],
    entry_points={"console_scripts": ["pipub=pipub.cli:run"]},
)
