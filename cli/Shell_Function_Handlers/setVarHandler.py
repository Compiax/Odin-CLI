###########################################################
#   File Details
###########################################################
#   Provides additional support to the shell for the setting
#   variable.
#   Created by Kyle Erwin - 20/07/2017
from MatrixTree.Matrix import Matrix
from printColors import *
from random import randint


class SetVarHandler():
    args = []
    isSetRandomBool = False

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

        if not str(self.args[0]).isalpha():
            valid = False

        if "random" in self.args:
            self.isSetRandomBool = True

            if len(self.args) != 4:
                valid = False

            if str(self.args[1]) != "random":
                valid = False

            if not str(self.args[2]).isdigit():
                valid = False

            if not str(self.args[3]).isdigit():
                valid = False

        else:
            if len(self.args) > 1:
                valid = False

        if errorMessage and not valid:
            print(PrintColors.FAIL + "ERROR: Invalid input." + PrintColors.ENDC)
            print(PrintColors.OKBLUE + "set [name]" + PrintColors.ENDC)
            print(PrintColors.OKBLUE + "set [name] random [minimum range vale] [maximum range vale]" + PrintColors.ENDC)

        return valid

    ###########################################################
    #   Get Methods
    ###########################################################
    def getName(self):
        return self.args[0]

    def isSetRandom(self):
        return self.isSetRandomBool

    ###########################################################
    #   Input Values
    ###########################################################
    def inputValues(self, dimensions):
        tree = Matrix()
        tree.build(dimensions)
        points = tree.getPoints()

        values = []

        for point in points:
            value = "AAAA"
            while str(value).isalpha():
                value =  input("Enter value for point " + str(point) + ": ")

                if str(value).isalpha():
                    print(PrintColors.FAIL + "ERROR: Please enter numerical value" + PrintColors.ENDC)

            values.append(value)

        tree.detlete()
        return values

    def randomValues(self, dimensions):
        if not self.isSetRandom():
            return

        numberOfPoints = 1

        for dimension in dimensions:
            numberOfPoints *= int(dimension)

        count = 0
        values = []
        min = float(self.args[2])
        max = float(self.args[3])

        while count < numberOfPoints:
            # random value int the range of minimum (args[2]) to max (args[3])
            values.append(randint(min, max))
            count += 1

        return values


