###########################################################
#   File Details
###########################################################
#   Provides additional support to the shell for the deleting
#   variable.
#   Created by Kyle Erwin - 24/07/2017
from printColors import *
from MatrixTree.Matrix import Matrix


class PrintVarHandler():
    args = []
    def __init__(self, _args):
        _args = _args.split()
        self.args = _args

    ###########################################################
    #   Validation Methods
    ###########################################################
    def validateArguments(self, errorMessage):

        valid = True

        if len(self.args) == 0:
            return False

        if len(self.args) > 1:
            valid = False

        if not str(self.args[0]).isalpha():
            valid = False

        if errorMessage and not valid:
            print(PrintColors.FAIL + "ERROR: Invalid input." + PrintColors.ENDC)
            print(PrintColors.OKBLUE + "print [name]" + PrintColors.ENDC)

        return valid

    ###########################################################
    #   Get Methods
    ###########################################################
    def getName(self):
        return self.args[0]

    ###########################################################
    #   Print Methods
    ###########################################################
    def printValues(self, dimensions, values):
        tree = Matrix()
        tree.build(dimensions)
        points = tree.getPoints()
        count = 0

        for point in points:
            print(str(point) + ": " + str(values[count]))
            count += 1

        tree.detlete()