import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        sb_x = ttk.Scrollbar(master=self, orient="horizontal")
        sb_y = ttk.Scrollbar(master=self, orient="vertical")
        canvas = tk.Canvas(master=self, width=400, height=400, scrollregion=(0, 0, 500, 500))
        canvas.configure(yscrollcommand=sb_y.set)
        canvas.configure(xscrollcommand=sb_x.set)
        sb_x['command'] = canvas.xview
        sb_y['command'] = canvas.yview

        canvas.grid(row=0, column=0, sticky=tk.N)
        sb_x.grid(row=1, column=0, sticky=tk.EW)
        sb_y.grid(row=0, column=1, sticky=tk.NS)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sub_frame = ttk.Frame(master=canvas)
        self.sub_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.sub_frame, anchor="nw")
        self.sub_frame.grid(row=0, column=0, sticky=tk.N)


class CollapsableFrame(ttk.Frame):
    def __init__(self, master, title, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.collapsed = tk.IntVar()
        self.collapsed.set(0)
        title_frame = ttk.Frame(master=self)
        title_frame.pack(fill=tk.X, side=tk.TOP, pady=2)
        lbl = ttk.Label(master=title_frame, text=title)
        lbl.pack(side=tk.LEFT, padx=4)
        self.btn = ttk.Button(master=title_frame, text="▼", width=2, command=self.toggle)
        self.btn.pack(side=tk.RIGHT)
        self.sub_frame = ttk.Frame(master=self)
        self.sub_frame.pack(fill=tk.X, side=tk.TOP, pady=2)

    def toggle(self):
        if bool(self.collapsed.get()):
            self.sub_frame.pack(fill=tk.X, side=tk.TOP, pady=2)
            self.btn.configure(text="▲")
            self.collapsed.set(0)
        else:
            self.sub_frame.forget()
            self.btn.configure(text="▼")
            self.collapsed.set(1)


class TableFrame(CollapsableFrame):
    def __init__(self, master, title, items, *args, **kwargs):
        super().__init__(master, title, *args, **kwargs)
        columns = ("param", "value")
        cs1_tree = ttk.Treeview(master=self.sub_frame, show="", columns=columns, selectmode="none")
        cs1_tree.pack(fill=tk.BOTH)
        cs1_tree.column("#1", minwidth=100, width=200, stretch=tk.YES)
        cs1_tree.column("#2", minwidth=50, width=50, stretch=tk.NO)
        cs1_tree.config(height=5)
        for item in items:
            cs1_tree.insert("", tk.END, values=item, tags=item.__str__)


class Logger:
    textbox = None

    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox['state'] = 'normal'
        self.textbox.insert(tk.END, text)
        self.textbox['state'] = 'disabled'

    def writeln(self, text):
        self.textbox['state'] = 'normal'
        self.textbox.insert(tk.END, text + '\n')
        self.textbox['state'] = 'disabled'

    def flush(self):
        pass
