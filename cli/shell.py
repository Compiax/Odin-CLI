###########################################################
#   File Details
###########################################################
#   The CLI shell. Uses function handler libraries as well
#   as the var library to handle all the requests
#   Created by Jason van Hattum - --/07/2017
#   Updates: modularisation - Kyle Erwin 21/07/2017

from cmd import Cmd
from Shell_Function_Handlers.createVarHandler import createVarHandler
from builtins import print


class OdinShell(Cmd):
    def do_var(self, args):
        """Creates a variable."""
        print ("'var' called with arguments {}".format(repr(args)))
        args = args.split()
        handler = createVarHandler(args)
        if handler.validateArguments(True):
            print


    def do_set(self, args):
        """Sets a variable."""
        print ("'set' called with arguments {}".format(repr(args)))

    def do_do(self, args):
        """Performs an operation."""
        print ("'do' called with arguments {}".format(repr(args)))

    def do_execute(self, args):
        """Executes the session."""
        print ("'execute' called with arguments {}".format(repr(args)))

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting the Odin CLI Shell..")
        raise SystemExit