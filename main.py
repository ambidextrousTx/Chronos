"""
Chronos:
  Time tracking application
  Runs on the desktop
"""

from entity import Entity
from project import Project
from subproject import SubProject
from datetime import datetime

def initialize(entity):
    print 'Project name: '
    proj_name = raw_input()
    entity.project.name = proj_name
    print 'SubProject name: '
    subproj_name = raw_input()
    entity.subproject.name = subproj_name
    return

def set_stop_time(entity):
    entity.stop_time = datetime.now()

def display_summary(entity):
    print entity.start_time
    print entity.stop_time
    print entity.project.name
    print entity.subproject.name

def main():
    entity = Entity()
    initialize(entity)
    print 'Press the Enter key to terminate this time tracking ...'

    while True:
        enter = raw_input()
        if enter == '':
            set_stop_time(entity)
            break

    display_summary(entity)

if __name__ == '__main__':
    main()
