"""
Represents a project
"""

class Project(object):
    ''' Represents a project, with some basic characteristics. Just the name
    for now. More to be added later '''
    def __init__(self, name):
        self._name = name

    def get_name(self):
        ''' Getter for the private name '''
        return self._name

    def set_name(self, new_name):
        ''' Setter for the private name '''
        self._name = new_name

    name = property(get_name, set_name)
