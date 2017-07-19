#!/usr/bin/env python
import sys
import shell

def start_shell():
    prompt = shell.OdinShell()
    prompt.prompt = '> '
    prompt.cmdloop('> Welcome to the Odin CLI Shell...')

def start_package_stuff():
    #@todo: Package stuff. 
    print("@todo: Package stuff")

# Do the actual things
if __name__ == '__main__':
    if sys.argv[1] == "shell":
        start_shell()

    elif sys.argv[1] == "package":
        start_package_stuff()