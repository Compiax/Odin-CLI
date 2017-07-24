###########################################################
#   File Details
###########################################################
#   Contains the definition and implementation of the Operation object.
#   Created by Jason van Hattum - 23/07/2017

class Operation:
    """
    A Session object encapsulates the details of an operation between variables
    """

    def __init__(self, operation_name, operands, outputvar):
        self.operation_name = operation_name        # Addition, Multiplication, Subtraction, Division
        self.operands = operands              # List of operands from left to right
        self.outputvar = outputvar

    def print(self):
        return "Operation: {} with operands {}, outputting to {}".format(self.operation_name, self.operands, self.outputvar)

    def __str__(self):
        return "{} {} {}".format(self.operation_name.upper(), ' '.join(map(str,self.operands)), self.outputvar)