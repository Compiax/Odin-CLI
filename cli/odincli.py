#!/usr/bin/env python3
import sys
import shell
import logging

def start_shell():
    logging.debug("Starting shell")
    prompt = shell.OdinShell()
    prompt.prompt = '> '
    prompt.cmdloop('> Welcome to the Odin CLI Shell...')

def start_package_stuff():
    #@todo: Package stuff. 
    print("@todo: Package stuff")

# Do the actual things
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr,level=logging.DEBUG) # Set logging level
    if sys.argv[1] == "shell":
        start_shell()

    elif sys.argv[1] == "package":
        start_package_stuff()