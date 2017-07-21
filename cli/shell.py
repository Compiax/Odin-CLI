###########################################################
#   File Details
###########################################################
#   The CLI shell. Uses function handler libraries as well
#   as the var library to handle all the requests
#   Created by Jason van Hattum - --/07/2017
#   Updates: modularisation - Kyle Erwin 21/07/2017
#            implemented create variable
#            added function to list variables

from cmd import Cmd
from builtins import print

# Shell handlers
from Shell_Function_Handlers.createVarHandler import *
from Shell_Function_Handlers.listVarHandler import *

# Variable handlers
from Variable_Handler.variableHandler import *


class OdinShell(Cmd):
    variables = VariableHandler()

    def do_var(self, args):
        """Creates a variable."""
        print ("'var' called with arguments {}".format(repr(args)))
        handler = CreateVarHandler(args)

        if handler.validateArguments(True):
            name = handler.getName()
            dimensions = handler.getDimensions()
            flags = handler.getFlags()
            rank = handler.getRank()

            if self.variables.containsVariable(name):
                print(PrintColors.FAIL + "ERROR: Variable already exists" + PrintColors.ENDC)
            else:
                self.variables.addVariable(name, dimensions, rank, flags)
                print(PrintColors.OKBLUE + "Variable " + name + " created" + PrintColors.ENDC)


    def do_set(self, args):
        """Sets a variable."""
        print ("'set' called with arguments {}".format(repr(args)))

    def do_do(self, args):
        """Performs an operation."""
        print ("'do' called with arguments {}".format(repr(args)))

    def do_execute(self, args):
        """Executes the session."""
        print ("'execute' called with arguments {}".format(repr(args)))

    def do_listv(self, args):
        """Executes the session."""
        handler = ListVarHandler(args)

        if handler.validateArguments(True):
            self.variables.listVariables()

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting the Odin CLI Shell..")
        raise SystemExit