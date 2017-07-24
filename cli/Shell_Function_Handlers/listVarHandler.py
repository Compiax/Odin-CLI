###########################################################
#   File Details
###########################################################
#   Provides additional support to the shell for the listing
#   variables. So far this class only validates the command
#   but perhaps a filter parameter could be added
#   Created by Kyle Erwin - 20/07/2017

from printColors import *


class ListVarHandler():
    args = []
    def __init__(self, _args):
        _args = _args.split()
        self.args = _args

    ###########################################################
    #   Validation Methods
    ###########################################################
    def validateArguments(self, errorMessage):
        valid = True

        # required length is 0, no additional arguments
        if len(self.args) > 0:
            valid = False

        if errorMessage and not valid:
            print(PrintColors.FAIL + "ERROR: Invalid input." + PrintColors.ENDC)
            print(PrintColors.OKBLUE + "listv" + PrintColors.ENDC)

        return valid