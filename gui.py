from Tkinter import *

class Frontend(Frame):
    ''' The front end of the application '''

    def do_track(self):
        ''' Start the tracking '''
        print 'Tracking now ...', self

    def do_stop(self):
        ''' Stop tracking '''
        print 'Stopping now ...', self

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
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

if __name__ == '__main__':
    ROOT = Tk()
    APP = Frontend(master=ROOT)
    APP.mainloop()
    ROOT.destroy()

