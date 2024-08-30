import ttkbootstrap as ttk
import tkinter as tk
import sys, os, gc

from modules.ui import *
from modules.views.home import Home

APP_NAME = "Refractored Meme"
APP_THEME = "pulse"

class Root(ttk.Window):
    def __init__(self, *args,**kwargs):
        super().__init__()
        self.title(APP_NAME)
        ttk.Style(APP_THEME)

        try:
            os.chdir(sys._MEIPASS)
        except:
            pass

        home = Home(self)
        home.grid(column=0, row=0, sticky="nsew")

        centerUIWindows(self)
        self.protocol("WM_DELETE_WINDOW", self.__onClose)
    
    def __onClose(self):
        self.quit()
        self.destroy()

if __name__ == "__main__":
    root = Root()
    root.mainloop()