###########################################################
#   File Details
###########################################################
#   Provides additional support to the shell for the setting
#   variable.
#   Created by Kyle Erwin - 20/07/2017

from printColors import *


class setVarHandler():
    args = []
    def __init__(self, _args):
        self.args = _args

    ###########################################################
    #   Validation Methods
    ###########################################################
    def validateArguments(self, errorMessage):

        valid = True

        if errorMessage and not valid:
            print(PrintColors.FAIL + "Invalid input." + PrintColors.ENDC)
            print("Correct Format as follows...")
            print(PrintColors.OKBLUE + "set [name]" + PrintColors.ENDC)

        return valid

    ###########################################################
    #   Get Methods
    ###########################################################
    def getName(self):
        """

        :return:
        """
        return self.args[0]

    def getDimensions(self):
        """

        :return:
        """
        dimensions = []

        index = 1
        while index < len(self.args):
            if not self.args[index].isdigit():
                break
            dimensions.append(self.args[index])
            index += 1

        return dimensions

    def getFlags(self):
        """

        :return:
        """
        index = 1
        while index < len(self.args):
            if not self.args[index].isdigit():
                break
            index += 1

        flags = ""
        while index < len(self.args):
            flags += self.args[index]

        return flags

    ###########################################################
    #   Input Values
    ###########################################################
    def inputValues(self):
        """

        :return:
        """

        dimensions = self.getDimensions(self.args)

        for dimensionLength in dimensions:
            dimensionLength = dimensions[index]


            index += 1


        return self.args[0]