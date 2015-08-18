"""
Each Project can have multiple SubProjects
"""

class SubProject(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, n):
        self._name = n

    name = property(get_name, set_name)

