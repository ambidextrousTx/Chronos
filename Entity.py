"""
Represents a basic time entry
"""

from datetime import datetime
from project import Project
from subproject import SubProject

class Entity(object):
    ''' Represents a time entry containing a start time,
    a stop time, a project name, and a subproject name '''
    def __init__(self):
        self.start_time = datetime.now()
        self.stop_time = datetime.now()
        self.project = Project('')
        self.subproject = SubProject('')
