#!/usr/bin/env python3
import sys
import shell

def start_shell():
    " Starts the shell interface "
    prompt = shell.OdinShell()
    prompt.prompt = '> '
    prompt.cmdloop('> Welcome to the Odin CLI Shell...')

def start_package_stuff():
    " A placeholder for the package manager."
    print("@todo: Package stuff")

# Do the actual things
if __name__ == '__main__':
    # By default, start the shell
    if len(sys.argv) == 1:
        start_shell()
    if sys.argv[1] == "shell":
        start_shell()

    elif sys.argv[1] == "package":
        start_package_stuff()