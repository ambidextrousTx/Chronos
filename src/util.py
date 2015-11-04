"""
Chronos:
  Time tracking application
  Runs on the desktop
  Utility functions
"""

import csv

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

def write_results_to_file(entity):
    ''' Write out the results into a CSV file '''
    with open('timetracking.csv', 'w') as fho:
        csvwriter = csv.writer(fho, delimiter='\t')
        csvwriter.writerow([entity.project.get_name(),
                            entity.sub_project.get_name(),
                            entity.get_elapsed_time()])
