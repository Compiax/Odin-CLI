#!/usr/bin/env python3
import sys
import logging
import shell

def start_shell():
    " Starts the shell interface "
    logging.debug("Starting shell")
    prompt = shell.OdinShell()
    prompt.prompt = '> '
    prompt.cmdloop('> Welcome to the Odin CLI Shell...')

def start_package_stuff():
    " A placeholder for the package manager."
    print("@todo: Package stuff")

# Do the actual things
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG) # Set logging level
    if sys.argv[1] == "shell":
        start_shell()

    elif sys.argv[1] == "package":
        start_package_stuff()
