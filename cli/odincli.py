#!/usr/bin/env python3
import sys
import shell
import argparse

def start_package_stuff():
    " A placeholder for the package manager."
    print("@todo: Package stuff")

# Do the actual things
if __name__ == '__main__':
    # Get arguments
    parser = argparse.ArgumentParser(description='Odin Command Line Interface')
    parser.add_argument('-port', action="store", type=int, dest="port", default=8000, help="Set the port the Daemon is on. Default: 8000")
    parser.add_argument('-host', action="store", dest="hostname", default="localhost", help="Set the host the Daemon is on. Default: localhost")
    results = parser.parse_args()

    # By default, start the shell
    connectionDetails = {'hostname': results.hostname, 'port': results.port}
    prompt = shell.OdinShell(connectionDetails)
    prompt.prompt = '> '
    prompt.cmdloop('> Welcome to the Odin CLI Shell...')