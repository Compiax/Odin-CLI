Odin-CLI
=====================

Odin CLI is the command-line interface to interact with the [Odin deamon][Arbitrary case-insensitive reference text] service. It contains commands to create and assign variables, do operations and execute sessions, as well as a rudimentary package manager for components.

Build status:

| branch | status |
| ------ | ------ |
| master | @todo Add travis build status |
| dev    | @todo Add travis build status |

## Running the CLI
> Requires Python 3.

To run the deamon simply run `python3 cli/odincli.py [shell|packages]`. The arguments are:

- `shell`: Runs the shell.
- `packages`: Manages components. Does nothing for now.

## Using the Shell

Type `help` or `?` to get the list of commands that can be used. Type `quit` to exit the CLI.

[arbitrary case-insensitive reference text]: https://github.com/Albert-Prime/Odin-Daemon
