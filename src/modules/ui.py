import ttkbootstrap as ttk
import tkinter as tk

def UI_place_on_Grid(parent: ttk.Frame, layout: list, spadx:tuple=None):
    '''
    Some Overly Engineered Grid Placement
    Places UI elements from a layout list accordingly
        Parameter:
            parent (ttk.Frame): parent frame to have things placed
            layout (list[ttk.*]): list of ttk.* Widgets

        Example of layout list:
            self.Tabs2 =    [[SLabel, SCheck],
                            [SIpRadio],
                            [SIpAddLabel, SIpAddEntry, SIpConnect],
                            [SCOMRadio],
                            [None,SCOMButton]]

            * None will place nothing and move the following item in the next column
    '''

    WHITELIST_STICKY = [ttk.Label, ttk.LabelFrame, ttk.Notebook, ttk.Frame, ttk.Separator]
    WHITELIST_COLSPAN = [ttk.LabelFrame, ttk.Notebook, ttk.Frame]

    for row, elements in zip(range(len(layout)),layout):
        for column, element in zip(range(len(elements)), elements):
            # NOTE: Add whatever restrictions here
            sticky = tk.NSEW if type(element) in WHITELIST_STICKY else tk.NW
            columnspan = len(max(layout, key=len)) if type(element) in WHITELIST_COLSPAN or (column == len(elements)-1) else 1
            padx = (5,0) if column == 0 else (0,0)
            padx = (padx[1] + 5) if (column == len(elements)-1) else padx
            padx = spadx if spadx is not None else padx
            if element is not None:
                element.grid(row=row, column=column, columnspan = columnspan, sticky=sticky, padx=padx, pady=(5,5))

def WIN_Reconfigure(frame, orientation = "rc"):
    """
    Configures the frames col/row to be resizable @ weight 1
        Parameter:
            frame (ttk.Frame, ttk.Window): frame containing all the UI elements
            orientation (str): select orientation for reconfiguration
    """
    col, row = frame.size()
    if "r" in orientation or orientation is None:
        for r in range(row):
            frame.rowconfigure(r, weight=1)
    
    if "c" in orientation or orientation is None:
        for c in range(col):
            frame.columnconfigure(c, weight=1) 

def centerUIWindows(window):
    """
    Just centers a Tkinter window
    """
    window.update()
    window.update_idletasks()
    s_width, s_height = window.winfo_screenwidth(), window.winfo_screenheight()
    app_width, app_height = window.winfo_width(), window.winfo_height()
    window.overrideredirect()
    window.geometry(f"+{int(1/2 * s_width - 1/2 * app_width)}+{int(1/2 * s_height - 1/2 * app_height)}")

