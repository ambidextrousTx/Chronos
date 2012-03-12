"""
Represents a basic time entry
"""

from datetime import datetime
from Project import Project
from SubProject import SubProject

class Entity(object):
    def __init__(self):
        self.startTime = datetime.now()
        self.stopTime = datetime.now()
        self.project = Project('')
        self.subproject = SubProject('')
