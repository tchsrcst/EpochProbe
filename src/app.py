import tkinter as tk
import tkinter.ttk as ttk

from frames import TopFrame, MiddleFrame, BottomFrame
import context as cntx


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("EpochProbe")
        self.iconbitmap("icon.ico")

        cntx.style = ttk.Style()
        cntx.style.theme_use('default')
        self.resizable(True, True)
        self.minsize(800, 600)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        root_frame = ttk.Frame(master=self)
        root_frame.grid(row=0, column=0, sticky=tk.NSEW)
        root_frame.columnconfigure(0, weight=1)
        root_frame.rowconfigure(0, weight=0)
        root_frame.rowconfigure(1, weight=1)
        root_frame.rowconfigure(2, weight=1)

        top_frame = TopFrame(root_frame)

        middle_frame = MiddleFrame(root_frame)
        bottom_frame = BottomFrame(root_frame)
