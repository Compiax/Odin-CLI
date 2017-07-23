###########################################################
#   File Details
###########################################################
#   Contains a class that is used to store, add and remove
#   all of the variables used ny the CLI shell.
#   NOTE - This class is only for housing data not getting it
#   from the shell.
#   Created by Kyle Erwin - 21/07/2017

from Variable_Handler.variable import *

class VariableHandler():
    list = []

    ###########################################################
    #   Manipulation Methods
    ###########################################################
    def addVariable(self, _varName, _varDimensions, _varRank, _varFlags):
        var = Variable(_varName, _varDimensions, [], _varRank, _varFlags)
        self.list.append(var)

    def deleteVariable(self, varName):
        for var in self.list:
            if var.name == varName:
                self.list.remove(var)
                break

    ###########################################################
    #   Other Methods
    ###########################################################
    def containsVariable(self, varName):
        if not self.list:
            return False

        for var in self.list:
            if var.name == varName:
                return True

        return False


    def getVariable(self, varName):
        for var in self.list:
            if var.name == varName:
                return var

        return -1

    def listVariables(self):
        for var in self.list:
            print (var)