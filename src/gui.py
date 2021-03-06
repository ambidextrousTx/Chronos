import Tkinter as tk
from entity import Entity
import util

class Frontend(tk.Frame):
    ''' The front end of the application '''

    def do_track(self):
        ''' Start the tracking '''
        if self.entity.tracking == False:
            project_name = self.project.get()
            print project_name, 'Entered from the widget'
            subproject_name = self.subproject.get()
            print subproject_name, 'Entered from the widget'
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
        self.bye = tk.Button(self)
        self.bye['text'] = 'Quit'
        self.bye['fg'] = 'red'
        self.bye['command'] = self.quit
        self.bye.grid(row=0, column=0)

        name_enforcement = self.register(util.enforce_nonempty_in_widget)

        self.project = tk.Entry(self, validate='all',
                                validatecommand=(name_enforcement))
        self.project.grid(row=2, column=1)

        self.subproject = tk.Entry(self, validate='all',
                                   validatecommand=(name_enforcement))
        self.subproject.grid(row=2, column=3)

        self.track = tk.Button(self)
        self.track['text'] = 'Track'
        self.track['command'] = self.do_track
        self.track.grid(row=0, column=2)

        self.stop = tk.Button(self)
        self.stop['text'] = 'Stop'
        self.stop['command'] = self.do_stop
        self.stop.grid(row=0, column=4)

    def __init__(self, master=None):
        self.bye = None
        self.track = None
        self.stop = None
        self.entity = Entity()
        self.project = None
        self.subproject = None
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

if __name__ == '__main__':
    ROOT = tk.Tk()
    APP = Frontend(master=ROOT)
    APP.master.title('Chronos')
    APP.master.minsize(360, 240)
    APP.mainloop()
    ROOT.destroy()

