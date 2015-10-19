"""
Each Project can have multiple SubProjects
"""

class SubProject(object):
    ''' A sub project associated with a project '''
    def __init__(self, name):
        self._name = name

    def get_name(self):
        ''' Getter for the name '''
        return self._name

    def set_name(self, new_name):
        ''' Setter for the name '''
        self._name = new_name

    name = property(get_name, set_name)

