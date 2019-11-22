from tkinter import *


class WindowManager(object):

    # constructor
    def __init__(self, window_name=None, window_width=0, window_height=0):
        # Make window
        self.window_name = window_name
        self.window_width = window_width
        self.window_height = window_height
        self.window = Tk()
        self.window.title(self.window_name)
        self.window.geometry(str(self.window_height) + "x" + str(self.window_width))
        # Add canvas
        self.mainCanvas = Canvas(self.window, width=self.window_width, height=self.window_height)
        # Show window
        self.window.mainloop()

    def get_window(self):
        return self.window

    def get_canvas(self):
        return self.mainCanvas