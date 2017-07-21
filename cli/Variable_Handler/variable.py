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


class variable():
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
        data["dimensions"] = self.dimensions
        data["values"] = self.values
        data["rank"] = self.rank
        data["flags"] = self.flags
        json_data = json.dumps(data)
        return  json_data



