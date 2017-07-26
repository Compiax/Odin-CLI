###########################################################
#   File Details
###########################################################
#   Contains a class that is used to store, add and remove
#   all of the variables used ny the CLI shell.
#   NOTE - This class is only for housing data not getting it
#   from the shell.
#   Created by Kyle Erwin - 21/07/2017
#   Updates: added a deleteAll function

from Variable_Handler.variable import *

class VariableHandler:
    list = []

    ###########################################################
    #   Manipulation Methods
    ###########################################################
    def addVariable(self, _varName, _varDimensions, _varRank, _varFlags):
        numberOfPoints = 1

        for dimension in _varDimensions:
            numberOfPoints *= int(dimension)

        varValues = [];

        count = 0;
        while count < numberOfPoints:
            varValues.append(0);

        var = Variable(_varName, _varDimensions, varValues, _varRank, _varFlags)
        self.list.append(var)

    def deleteVariable(self, varName):
        for var in self.list:
            if var.name == varName:
                self.list.remove(var)
                break

    def deleteAll(self):
        del self.list[:]
        self.list = []

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

    def isEmpty(self):
        return len(self.list) == 0