# Pipub: Pipe data from the command line to Google Pubsub

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
[![PyPI version](https://badge.fury.io/py/pipub.svg)](https://badge.fury.io/py/pipub)

Pipub is a command line tool that makes it easy to stream data to Google Cloud Pubsub.

## Installation

To install `pipub`, simply run:

```bash
$ pip install pipub
```

## Quickstart

Before executing the command line tool you'll need a Google Cloud Project with a [Pubsub topic](https://cloud.google.com/pubsub/docs/admin).

Sending a local [new line delimited JSON file](http://ndjson.org/) to a Pubsub topic `test` is as simple as running:

```bash
$ cat file.json | pipub test -p project-name
```

Peam will take care of sending each line as a new message to the `test` topic.

This simplicity allows you to pipe the data to other programs before sending the data.
