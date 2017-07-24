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
from Shell_Function_Handlers.delVarHandler import DelVarHandler
from Shell_Function_Handlers.listVarHandler import *
from Shell_Function_Handlers.setVarHandler import SetVarHandler

# Variable handlers
from Variable_Handler.variableHandler import *

from session import Session

import Operations




class OdinShell(Cmd):
    session = Session()

    def do_var(self, args):
        """Creates a variable."""
        handler = CreateVarHandler(args)

        if handler.validateArguments(True):
            name = handler.getName()
            dimensions = handler.getDimensions()
            flags = handler.getFlags()
            rank = handler.getRank()

            if self.session.variables.containsVariable(name):
                print(PrintColors.FAIL + "ERROR: Variable already exists" + PrintColors.ENDC)
            else:
                self.session.variables.addVariable(name, dimensions, rank, flags)
                print(PrintColors.OKBLUE + "Variable " + name + " created" + PrintColors.ENDC)

    def do_set(self, args):
        """Sets a variable."""
        handler = SetVarHandler(args)

        if handler.validateArguments(True):
            name = handler.getName()

            if self.session.variables.containsVariable(name):
                variable = self.session.variables.getVariable(name)
                variable.values = handler.inputValues(variable.dimensions)
                print(PrintColors.OKBLUE + "Values set to variable " + name + PrintColors.ENDC)
            else:
                print(PrintColors.FAIL + "ERROR: No such variable exists" + PrintColors.ENDC)

    def do_p(self, args):
        self.session.print()

    def do_do(self, args):
        """Performs an operation."""
        Operations.validate_arguments_and_add(self.session, args)

    def do_execute(self, args):
        """Executes the session."""
        self.session.execute_session()

    def do_listv(self, args):
        handler = ListVarHandler(args)

        if handler.validateArguments(True):
            self.variables.listVariables()

    def do_del(self, args):
        handler = DelVarHandler(args)

        if handler.validateArguments(True):
            name = handler.getName()
            if self.variables.containsVariable(name):
                self.variables.deleteVariable(name)
                print(PrintColors.OKBLUE + "Variable " + name + " deleted" + PrintColors.ENDC)
            else:
                print(PrintColors.FAIL + "ERROR: No such variable exists" + PrintColors.ENDC)

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting the Odin CLI Shell..")
        raise SystemExit