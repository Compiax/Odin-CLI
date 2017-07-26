###########################################################
#   File Details
###########################################################
#   Contains a class called var which be used a an object
#   to store all the variable information input from the
#   shell.
#   NOTE - This class is only for housing data not getting it
#   from the shell.
#   Created by Kyle Erwin - 21/07/2017

import json


class Variable():
    name = ""
    dimensions = []
    values = []
    rank = 0
    flags = ""

    def __init__(self, _name, _dimensions, _values, _rank, _flags):
        self.name = _name
        self.dimensions = _dimensions
        self.values = _values
        self.rank = _rank
        self.flags = _flags

    def copy(self, _name, _flags):
        copyVar = var(_name, self.dimensions, self.values, self.rank, _flags)
        return copyVar

    def convertToJson(self):
        data = {}
        data["name"] = self.name
        data["dimensions"] = list(map(int, self.dimensions))
        data["values"] = list(map(int, self.values))
        print(data["values"])
        data["rank"] = self.rank
        data["save"] = self.flags
        json_data = json.dumps(data)
        return  json_data

    def __str__(self):
        return "Variable: " + self.name




