from printColors import *

###########################################################
#   File Details
###########################################################
#   Provides additional support to the shell such as validation of input
#   to avoid clutter.
#   Created by Kyle Erwin - 19/07/2017

###########################################################
#   Validation Methods
###########################################################
def validateCreateVarInput(args, errorMessage):
    """
    To determine if the args past through the shell is valid to create a variable
    :param args: array, the arguments from the shell
    :param errorMessage: bool, to decide if we must output the error message
    :return: bool
    """
    valid = True

    if len(args) == 1:
        valid = False

    if not str(args[0]).isalpha():
        valid = False

    index = 1

    if "--save" not in args:
        while index < len(args):
            if not args[index].isdigit():
                valid = False
            index += 1
    else:
        while index < len(args) - 1:
            if not str(args[index]).isdigit():
                valid = False
            index += 1

        if str(args[len(args) - 1]) == "--save":
            valid = False

    if errorMessage and not valid:
        print(PrintColors.FAIL + "Invalid input." + PrintColors.ENDC)
        print("Correct Format as follows...")
        print(PrintColors.OKBLUE + "var [name] [dimensions] <flags>" + PrintColors.ENDC)

    return valid
