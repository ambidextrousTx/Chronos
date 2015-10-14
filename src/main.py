"""
Chronos:
  Time tracking application
  Runs on the desktop
"""

from entity import Entity

def initialize(entity):
    ''' Initialize the app '''
    print 'Project name: '
    proj_name = raw_input()
    while proj_name == '':
        print 'Cannot be empty!'
        print 'Project name: '
        proj_name = raw_input()
    entity.set_project(proj_name)
    print 'SubProject name: '
    subproj_name = raw_input()
    while subproj_name == '':
        print 'Cannot be empty!'
        print 'SubProject name: '
        subproj_name = raw_input()
    entity.set_subproject(subproj_name)
    entity.start()
    return

def set_stop_time(entity):
    ''' Stop timing it now '''
    entity.stop()

def display_summary(entity):
    ''' Tabulate the summary of the tracking '''
    print 'Getting total time elapsed'
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

if __name__ == '__main__':
    main()
