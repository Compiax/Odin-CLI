###########################################################
#   File Details
###########################################################
#   Provides additional support to the shell for the creating
#   variable.
#   Created by Kyle Erwin - 20/07/2017

from printColors import *


class createVarHandler():
    args = []
    def __init__(self, _args):
        self.args = _args

    ###########################################################
    #   Validation Methods
    ###########################################################
    def validateArguments(self, errorMessage):
        """
        To determine if the args past through the shell is valid to create a variable
        :param args: array, the arguments from the shell
        :param errorMessage: bool, to decide if we must output the error message
        :return: bool
        """
        valid = True

        # minimum length is 2
        if len(self.args) <= 1:
            valid = False

        if not str(self.args[0]).isalpha():
            valid = False

        index = 1

        if "--save" not in self.args:
            while index < len(self.args):
                if not self.args[index].isdigit():
                    valid = False
                    break
                index += 1
        else:
            while index < len(self.args) - 1:
                if not str(self.args[index]).isdigit():
                    valid = False
                    break
                index += 1

            if str(self.args[len(self.args) - 1]) == "--save":
                valid = False

        if errorMessage and not valid:
            print(PrintColors.FAIL + "Invalid input." + PrintColors.ENDC)
            print("Correct Format as follows...")
            print(PrintColors.OKBLUE + "var [name] [dimensions] <flags>" + PrintColors.ENDC)

        return valid