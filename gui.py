from Tkinter import *
from entity import Entity

class Frontend(Frame):
    ''' The front end of the application '''

    def do_track(self):
        ''' Start the tracking '''
        if self.entity.tracking == False:
            print 'Enter the project name '
            project_name = raw_input()
            print 'Enter the subproject name '
            subproject_name = raw_input()
            self.entity.set_project(project_name)
            self.entity.set_subproject(subproject_name)
            self.entity.start()
            self.entity.tracking = True
            print 'Tracking now ...', self
        else:
            print 'Already tracking ...'

    def do_stop(self):
        ''' Stop tracking '''
        if self.entity.tracking == True:
            print 'Stopping now ...', self
            self.entity.stop()
            print 'Tracked total time %s' % self.entity.get_elapsed_time()
            print 'Project %s' % self.entity.project.get_name()
            print 'Sub-Project %s' % self.entity.sub_project.get_name()
        else:
            print 'Not tracking anything ...'

    def create_widgets(self):
        ''' Intialize widgets '''
        self.bye = Button(self)
        self.bye['text'] = 'Quit'
        self.bye['fg'] = 'red'
        self.bye['command'] = self.quit
        self.bye.pack({'side': 'left'})

        self.track = Button(self)
        self.track['text'] = 'Track'
        self.track['command'] = self.do_track
        self.track.pack({'side': 'left'})

        self.stop = Button(self)
        self.stop['text'] = 'Stop'
        self.stop['command'] = self.do_stop
        self.stop.pack({'side': 'left'})

    def __init__(self, master=None):
        self.bye = None
        self.track = None
        self.stop = None
        self.entity = Entity()
        Frame.__init__(self, master)
        self.pack(expand=1)
        self.create_widgets()

if __name__ == '__main__':
    ROOT = Tk()
    APP = Frontend(master=ROOT)
    APP.master.title('Chronos')
    APP.master.minsize(640, 480)
    APP.mainloop()
    ROOT.destroy()

