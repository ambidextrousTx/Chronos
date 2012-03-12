"""
Chronos:
  Time tracking application
  Runs on the desktop
"""

from Entity import Entity
from Project import Project
from SubProject import SubProject
from datetime import datetime

def initialize(entity):
    print 'Project name: '
    proj_name = raw_input()
    entity.project.name = proj_name
    print 'SubProject name: '
    subproj_name = raw_input()
    entity.subproject.name = subproj_name
    return

def setStopTime(entity):
    entity.stopTime = datetime.now()

def displaySummary(entity):
    print entity.startTime
    print entity.stopTime
    print entity.project.name
    print entity.subproject.name

def main():
    entity = Entity()
    initialize(entity)
    print 'Press the Enter key to terminate this time tracking ...'

    while True:
        enter = raw_input()
        if enter == '':
            setStopTime(entity)
            break

    displaySummary(entity)

if __name__ == '__main__':
    main()
