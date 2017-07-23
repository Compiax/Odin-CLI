###########################################################
#   File Details
###########################################################
#   Provides additional support to the shell for the deleting
#   variable.
#   Created by Kyle Erwin - 22/07/2017
from printColors import *

class DelVarHandler():
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
            print(PrintColors.FAIL + "Invalid input." + PrintColors.ENDC)
            print("Correct Format as follows...")
            print(PrintColors.OKBLUE + "del [name]" + PrintColors.ENDC)

        return valid

    ###########################################################
    #   Get Methods
    ###########################################################
    def getName(self):
        return self.args[0]