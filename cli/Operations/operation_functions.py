###########################################################
#   File Details
###########################################################
#   Contains functions used to manage Operation objects
#   Created by Jason van Hattum - 23/07/2017

from printColors import *
from .operation import Operation

def add_operation(session, operation_name, operands):
    """
    Adds an operation to the current session
    """
    operation = Operation(operation_name, operands[:-1], operands[-1])
    session.operations.append(operation)
    return operation

def validate_arguments_and_add(session, args):
    """
    Validates the arguments passed in to a 'do' command.
    Arguments should be in the format 'do [operation_name] [operand <, operand>]
    operation_name must be mul, sub, add, div
    Returns a dict with the fields 'operation_name' and 'operands'
    """
    args = args.split()
    numargs = len(args)
    operation_name = args[0]
    operands = args[1:]

    # Basic operation
    if (operation_name in ["sum", "mul", "sub", "div", "mult", "div"]):
        if (len(operands) == 3):
            operandItems = []
            for operand in operands:
                if not (session.variables.containsVariable(operand)):
                    print("Error: {}Variable {} does not exist.{}".format(PrintColors.FAIL,operand,PrintColors.ENDC))
                    return
                operandItems.append(session.variables.getVariable(operand))
            op = add_operation(session, operation_name, operandItems)
            print("{}Added {} operation between {} and {}, outputting to {}{}".format(PrintColors.OKBLUE,
                                                                                      op.operation_name.upper(),
                                                                                      op.operands[0],
                                                                                      op.operands[1],
                                                                                      op.outputvar,
                                                                                      PrintColors.ENDC))
        else:
            error("Incorrect number of arguments passed to {}, should be 2.".format(operation_name))
    elif (operation_name in ["abs"]):
        if (len(operands) == 2):
            operandItems = []
            for operand in operands:
                if not (session.variables.containsVariable(operand)):
                    print("Error: {}Variable {} does not exist.{}".format(PrintColors.FAIL,operand,PrintColors.ENDC))
                    return
                operandItems.append(session.variables.getVariable(operand))
            op = add_operation(session, operation_name, operandItems)
            print("{}Added {} operation between {}, outputting to {}{}".format(PrintColors.OKBLUE,
                                                                                      op.operation_name.upper(),
                                                                                      op.operands[0],
                                                                                      op.outputvar,
                                                                                      PrintColors.ENDC))
        else:
            error("Incorrect number of arguments passed to {}, should be 1.".format(operation_name))
    else:
        component = next((x for x in session.components if x.component_name == operation_name), None)
        if not component is None:
            # Component is installed
            if component.num_operands == (len(operands) - 1):
                operandItems = []
                for operand in operands:
                    if not (session.variables.containsVariable(operand)):
                        print("Error: {}Variable {} does not exist.{}".format(PrintColors.FAIL,operand,PrintColors.ENDC))
                        return
                    operandItems.append(session.variables.getVariable(operand))
                op = add_operation(session, operation_name, operandItems)
                print("{}Added {} operation between {} and {}, outputting to {}{}".format(PrintColors.OKBLUE,
                                                                                      op.operation_name.upper(),
                                                                                      op.operands[0],
                                                                                      op.operands[1],
                                                                                      op.outputvar,
                                                                                      PrintColors.ENDC))
            else:
                print("Not correct number of operands")
        else:
            print("{}{} is not a valid operation. Do you have that component installed?{}".format(PrintColors.OKBLUE,
                                                                                              operation_name,
                                                                                              PrintColors.ENDC))

def error(e):
    print(PrintColors.FAIL + e + PrintColors.ENDC)
    print("Correct format:")
    print(PrintColors.OKBLUE + "do [operation] [operands]" + PrintColors.ENDC)
