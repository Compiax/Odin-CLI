from printColors import *

def validateCreateVarInput(args, errorMessage):
    valid = True

    if not len(args) == 1:
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
        print("For Example.")
        print("var network 3 2 --save")
        print("(please note that the --save is optional)")

    return valid
