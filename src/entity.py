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
        self.elapsed_time = None
        self.project = None
        self.sub_project = None

    def set_project(self, project_name):
        ''' Set the project name. Currently setting it like this.
        Susceptible for cleanup later '''
        self.project = Project(project_name)

    def set_subproject(self, subproject_name):
        ''' Set the subproject name. Currently setting it like this.
        Susceptible for cleanup later '''
        self.sub_project = SubProject(subproject_name)

    def get_elapsed_time(self):
        ''' Compute the difference/ delta between the stop and start time '''
        if self.tracking == True:
            return 'Still tracking!'
        else:
            return self.elapsed_time

    def start(self):
        ''' Called when the tracking begins '''
        self.start_time = datetime.now()
        self.tracking = True

    def stop(self):
        ''' Called when the tracking ends '''
        self.stop_time = datetime.now()
        self.tracking = False
        self.elapsed_time = self.stop_time - self.start_time
