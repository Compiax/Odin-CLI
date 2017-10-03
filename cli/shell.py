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

from session import Session

import Operations
import Components




class OdinShell(Cmd):
    
    
    ###########################################################
    #   Createing/setting vars
    ###########################################################
    def __init__(self, connectionDetails):
        super(OdinShell, self).__init__()
        self.session = Session(connectionDetails)
        self.session.components = Components.initialize_components()
        print("> {}Loaded components: {}{}".format(PrintColors.OKBLUE,', '.join(map(str,self.session.components)),PrintColors.ENDC))

    def do_var(self, args):
        """
        Creates a variable.
        Usage: var [name] [dimensions] <flags>
        """
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
        """
        Sets the value of a variable.
        Usage: set [variable]
        """
        handler = SetVarHandler(args)

        if handler.validateArguments(True):
            name = handler.getName()

            if self.session.variables.containsVariable(name):
                variable = self.session.variables.getVariable(name)

                if handler.isSetRandom():
                    variable.values = handler.randomValues(variable.dimensions)
                else:
                    variable.values = handler.inputValues(variable.dimensions)
                print(PrintColors.OKBLUE + "Values set to variable " + name + PrintColors.ENDC)
            else:
                print(PrintColors.FAIL + "ERROR: No such variable exists" + PrintColors.ENDC)

    def do_p(self, args):
        """
        Prints EVERYTHING.
        Usage: p
        """
        self.session.print()

    ###########################################################
    #   Deletes
    ###########################################################
    def do_del(self, args):
        """
        Deletes a variable.
        Usage: del [variable]
        """
        handler = DelVarHandler(args)

        if handler.validateArguments(True):
            name = handler.getName()
            if self.session.variables.containsVariable(name):
                self.session.variables.deleteVariable(name)
                print(PrintColors.OKBLUE + "Variable " + name + " deleted" + PrintColors.ENDC)
            elif name == "*":
                self.session.variables.deleteAll()
                print(PrintColors.OKBLUE + "All variables deleted" + PrintColors.ENDC)
            else:
                print(PrintColors.FAIL + "ERROR: No such variable exists" + PrintColors.ENDC)

    ###########################################################
    #   Perform actions
    ###########################################################

    def do_listv(self, args):
        """
        Lists all variables.
        Usage: listv
        """
        handler = ListVarHandler(args)

        if handler.validateArguments(True):
            if self.session.variables.isEmpty():
                print(PrintColors.OKBLUE + "No variables" + PrintColors.ENDC)
            else:
                self.session.variables.listVariables()

    def do_print(self, args):
        """
        Prints the details of a variable. 
        Usage: print [variable]
        """
        handler = PrintVarHandler(args)

        if handler.validateArguments(True):
            name = handler.getName()
            if self.session.variables.containsVariable(name):
                variable = self.session.variables.getVariable(name)
                handler.printValues(variable.dimensions, variable.values)
            else:
                print(PrintColors.FAIL + "ERROR: No such variable exists" + PrintColors.ENDC)

    def do_execute(self, args):
        """
        Executes the session.
        """
        self.session.execute()

    def do_do(self, args):
        """
        Performs an operation
        """
        Operations.validate_arguments_and_add(self.session,args)

    ##########################################################
    #   Write/reading files (export/import)
    ###########################################################
    def do_export(self, args):
        """Exports the current variables to a file."""
        print ("'export' called with arguments {}".format(repr(args)))

    def do_import(self, args):
        """Imports the current variables from a file."""
        print ("'import' called with arguments {}".format(repr(args)))

    ###########################################################
    #   Quit
    ###########################################################

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting the Odin CLI Shell..")
        self.session.close()
        raise SystemExit