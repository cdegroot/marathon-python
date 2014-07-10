#!/usr/bin/env python
"""Mesosphere Marathon command-line client. Very minimal as it is a WIP

Commands:
  ls - show running applications
  create - create a new application. Json can be a single argument or read from stdin

Usage:
  marathon ls [<app>]
  marathon create [<json>]

The environment variable MARATHON must point to a marathon instance.

"""
from docopt import docopt
from marathon import MarathonClient
import os


def do_ls(marathonClient, app):
    apps = marathonClient.list_apps(id=app) if app else marathonClient.list_apps()

    for appInfo in apps:
        print appInfo.json_encode()


def do_create(marathonClient, json):
    jsonString = sys.stdin.readlines.join('') if not json else json
    appData = json.loads(jsonString)

    marathonClient.create_app(appData)


if __name__ == '__main__':
    marathon_url = os.environ['MARATHON']
    marathonClient = MarathonClient(marathon_url)
    arguments = docopt(__doc__)
    print arguments
    if arguments.has_key('ls'):
        do_ls(marathonClient, arguments.get('<app>', None))
    elif arguments.has_key('create'):
        do_create(marathonClient, arguments.get('<json>', None))