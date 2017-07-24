###########################################################
#   File Details
###########################################################
#   Contains the definition and implementation of the Component object.
#   Created by Jason van Hattum - 24/07/2017

class Component:
    """
    A Component object is a component of a computational flow, that can be used as an operation.
    """

    def __init__(self, component_name, num_operands):
        self.component_name = component_name
        self.num_operands = num_operands

    def print(self):
        return "Component: {} with {} operands.".format(self.component_name.upper(), self.num_operands)

    def __str__(self):
        return self.component_name