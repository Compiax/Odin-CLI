###########################################################
#   File Details
###########################################################
#   Contains the definition and implementation of the Session object.
#   Created by Jason van Hattum - 23/07/2017

from Variable_Handler.variableHandler import *

class Session:
    """
    A Session object will contain the variables and operations of the current session
    """
    # variables = []
    # operations = []

    def __init__(self):
        self.variables = VariableHandler()
        self.operations = []

    def execute_session(self):
        """
        Executes the session, sending all variables and operations to the Daemon
        """
       

    def print(self):
        print("Variables:")
        for var in self.variables.list:
            print("- {}".format(var.convertToJson()))
        print("Operations:")
        for op in self.operations:
            print("- {}".format(op))
