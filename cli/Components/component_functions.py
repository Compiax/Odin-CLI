###########################################################
#   File Details
###########################################################
#   Contains functions used to manage Component objects
#   Created by Jason van Hattum - 24/07/2017

from printColors import *
from .component import Component
from pathlib import Path
import glob, os
import json

def initialize_components():
    """
    Finds all components in some directory.
    @TODO: Clean this function  up. It's disgusting
    """
    for root, dirs, files in os.walk("./components", topdown=False):
        components = []
        for name in dirs:
            path = os.path.join(root, name)
            path = os.path.join(path, "component.json")
            component_file = Path(path)
            if component_file.is_file():
                with open(path) as json_data:
                    data = json.load(json_data)
                    # @TODO: Validate the JSON file
                    components.append(Component(data['name'], data['inputs']['amount']))
    return components    