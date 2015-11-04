"""
Chronos:
  Time tracking application
  Runs on the desktop
"""

import util
from entity import Entity

def initialize(entity):
    ''' Initialize the app '''

    print 'Project name: '
    proj_name = util.enforce_nonempty_name()
    entity.set_project(proj_name)

    print 'SubProject name: '
    subproj_name = util.enforce_nonempty_name()
    entity.set_subproject(subproj_name)

    entity.start()
    return

def set_stop_time(entity):
    ''' Stop timing it now '''
    entity.stop()

def display_summary(entity):
    ''' Tabulate the summary of the tracking '''
    print 'Project name: %s' % entity.project.get_name()
    print 'Sub-project name: %s' % entity.sub_project.get_name()
    print 'Start time: %s' % entity.start_time
    print 'End time: %s' % entity.stop_time
    print 'Computing total time elapsed'
    print entity.get_elapsed_time()

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
    util.write_results_to_file(entity)

if __name__ == '__main__':
    main()
