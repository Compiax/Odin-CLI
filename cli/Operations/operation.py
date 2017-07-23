###########################################################
#   File Details
###########################################################
#   Contains the definition and implementation of the Operation object.
#   Created by Jason van Hattum - 23/07/2017

class Operation:
    """
    A Session object encapsulates the details of an operation between variables
    """

    def __init__(self):
        self.operation_name = ""        # Addition, Multiplication, Subtraction, Division
        self.operands = []              # List of operands from left to right

    def print(self):
        return "{} with operands {}".format(self.operation_name, self.operands)
