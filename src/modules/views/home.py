import ttkbootstrap as ttk
import tkinter as tk
from random import randint
from modules.ui import *

class Home(ttk.Frame):
    def __init__(self, parent:ttk.Window, *args, **kwargs):
        super().__init__(parent)
        self.parent = parent
        self.__buildLayout()
        self.__bindLayout()

    def __buildLayout(self):
        self.interactables = {}
        self.interactables["button"] = ttk.Button(self, text="PRESS ME", width=30, padding=10)

        layout = [
            [ttk.Label(self, text="Hello, please press on the button below to roll the 100 sided dice", wraplength=200)],
            [self.interactables["button"]]
        ]

        UI_place_on_Grid(self, layout=layout, spadx=(5,5))


    def __bindLayout(self):
        self.interactables["button"].configure(command=self.changeButtonText)

    def changeButtonText(self):
        self.interactables["button"].configure(text=str(randint(1, 100)))