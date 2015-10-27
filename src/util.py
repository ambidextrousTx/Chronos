"""
Chronos:
  Time tracking application
  Runs on the desktop
  Utility functions
"""

def enforce_nonempty_name():
    ''' Enforce a non empty project or subproject name '''
    proj_name = raw_input()
    while proj_name == '':
        print 'Cannot be empty!'
        print 'Name: '
        proj_name = raw_input()
    return proj_name

def enforce_nonempty_in_widget(name):
    ''' Enforce a non empty name in a widget '''
    return name != ''
