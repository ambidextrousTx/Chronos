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
        self.tracking = False
        self.start_time = None
        self.stop_time = None
        self.project = Project('')
        self.subproject = SubProject('')

    def compute_elapsed_time(self):
        ''' Compute the difference/ delta between the stop and start time '''
        return self.stop_time - self.start_time

    def start(self):
        ''' Called when the tracking begins '''
        self.start_time = datetime.now()
        self.tracking = True

    def stop(self):
        ''' Called when the tracking ends '''
        self.stop_time = datetime.now()
        self.tracking = False

