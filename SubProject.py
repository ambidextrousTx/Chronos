"""
Each Project can have multiple SubProjects
"""

class SubProject(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self._name
        
    def setName(self, n):
        self._name = n

    name = property(getName, setName)

