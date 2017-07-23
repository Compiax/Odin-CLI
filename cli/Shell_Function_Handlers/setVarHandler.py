###########################################################
#   File Details
###########################################################
#   Provides additional support to the shell for the setting
#   variable.
#   Created by Kyle Erwin - 20/07/2017

from printColors import *


class SetVarHandler():
    args = []
    def __init__(self, _args):
        _args = _args.split()
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
    #   Input Values
    ###########################################################
    def inputValues(self):
        return True