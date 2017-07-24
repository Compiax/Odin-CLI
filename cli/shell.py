###########################################################
#   File Details
###########################################################
#   The CLI shell. Uses function handler libraries as well
#   as the var library to handle all the requests
#   Created by Jason van Hattum - --/07/2017
#   Updates: modularisation - Kyle Erwin 21/07/2017
#            implemented create variable
#            added function to list variables
#            added function to delete variable
#            added function to export variable

from cmd import Cmd
from builtins import print

# Shell handlers
from Shell_Function_Handlers.createVarHandler import *
from Shell_Function_Handlers.delVarHandler import DelVarHandler
from Shell_Function_Handlers.listVarHandler import *
from Shell_Function_Handlers.printVarHandler import PrintVarHandler
from Shell_Function_Handlers.setVarHandler import SetVarHandler

# Variable handlers
from Variable_Handler.variableHandler import *


class OdinShell(Cmd):
    variables = VariableHandler()

    ###########################################################
    #   Createing/setting vars
    ###########################################################

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
        handler = SetVarHandler(args)

        if handler.validateArguments(True):
            name = handler.getName()

            if self.variables.containsVariable(name):
                variable = self.variables.getVariable(name)

                if handler.isSetRandom():
                    variable.values = handler.randomValues(variable.dimensions)
                else:
                    variable.values = handler.inputValues(variable.dimensions)

                print(PrintColors.OKBLUE + "Values set to variable " + name + PrintColors.ENDC)
            else:
                print(PrintColors.FAIL + "ERROR: No such variable exists" + PrintColors.ENDC)

    ###########################################################
    #   Deletes
    ###########################################################
    def do_del(self, args):
        handler = DelVarHandler(args)

        if handler.validateArguments(True):
            name = handler.getName()
            if self.variables.containsVariable(name):
                self.variables.deleteVariable(name)
                print(PrintColors.OKBLUE + "Variable " + name + " deleted" + PrintColors.ENDC)
            elif name == "*":
                self.variables.deleteAll()
                print(PrintColors.OKBLUE + "All variables deleted" + PrintColors.ENDC)
            else:
                print(PrintColors.FAIL + "ERROR: No such variable exists" + PrintColors.ENDC)

    ###########################################################
    #   Perform actions
    ###########################################################
    def do_do(self, args):
        """Performs an operation."""
        print("'do' called with arguments {}".format(repr(args)))

    def do_execute(self, args):
        """Executes the session."""
        print("'execute' called with arguments {}".format(repr(args)))

    def do_listv(self, args):
        handler = ListVarHandler(args)

        if handler.validateArguments(True):
            if self.variables.isEmpty():
                print(PrintColors.OKBLUE + "No variables" + PrintColors.ENDC)
            else:
                self.variables.listVariables()

    def do_print(self, args):
        handler = PrintVarHandler(args)

        if handler.validateArguments(True):
            name = handler.getName()
            if self.variables.containsVariable(name):
                variable = self.variables.getVariable(name)
                handler.printValues(variable.dimensions, variable.values)
                print(PrintColors.OKBLUE + "Variable " + name + " deleted" + PrintColors.ENDC)
            else:
                print(PrintColors.FAIL + "ERROR: No such variable exists" + PrintColors.ENDC)

    ##########################################################
    #   Write/reading files (export/import)
    ###########################################################
    def do_export(self, args):
        """Executes the session."""
        print ("'execute' called with arguments {}".format(repr(args)))

    def do_import(self, args):
        """Executes the session."""
        print ("'execute' called with arguments {}".format(repr(args)))

    ###########################################################
    #   Quit
    ###########################################################

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting the Odin CLI Shell..")
        raise SystemExit