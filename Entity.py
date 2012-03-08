"""
Represents a basic time entry
"""

from datetime import datetime
from Project import Project

class Entity(object):
    def __init__(self):
        self.startTime = datetime.now()
        self.stopTime = dateTime.now()
        self.project = Project('', '')
