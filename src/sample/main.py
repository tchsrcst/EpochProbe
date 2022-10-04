import tkinter as tk
import tkinter.ttk as ttk
import sys

from util import save_manager
from gui import Logger, ScrollableFrame, TableFrame
from stats import *

import input
import plot
from skill import skills
from affix import affixes
from scenario import scenarios


class App(tk.Tk):
    skill = skills.Fireball
    scenario = scenarios.BasicScenario
    base = input.InputBase
    input = base
    logger = None
    style = None
    version = '0.1'
    sm = save_manager.SaveManager()
    content = None
    text_box = None

    def get_themes(self):
        return self.style.theme_names()

    def set_theme(self, t):
        self.style.theme_use(t)

    def click(self):
        pass

    def top(self, parent):
        btn_1 = ttk.Button(master=parent, text="btn1", width=8)
        btn_1.grid(row=0, column=0, sticky=tk.N)
        btn_2 = ttk.Button(master=parent, text="btn2", width=8)
        btn_2.grid(row=0, column=1, sticky=tk.N)

        v_character_slot = tk.StringVar()
        v_character_slot.set('CharacterSlot')
        om_character_slot = ttk.OptionMenu(parent, v_character_slot, *self.sm.filenames)
        om_character_slot.config(width=25)
        om_character_slot.grid(row=0, column=2, sticky=tk.N)

        v_gui_theme = tk.StringVar()
        om_gui_theme = ttk.OptionMenu(parent, v_gui_theme, *self.get_themes(), command=self.set_theme)
        v_gui_theme.set('default')
        om_gui_theme.config(width=6)
        om_gui_theme.grid(row=0, column=3, sticky=tk.NE)

    def left(self, parent):
        options_frame = ttk.Frame(parent)
        options_frame.pack(padx=4, pady=4)

        scenario_label = ttk.Label(master=options_frame, text="Scenario", width=12, anchor="e", justify=tk.LEFT)
        scenario_label.grid(row=1, column=0, padx=5)
        v_scenario = tk.StringVar()
        om_scenario = ttk.OptionMenu(options_frame, v_scenario, *scenarios.scenarios_dict.keys())
        om_scenario.config(width=25)
        om_scenario.grid(row=1, column=1)

        skill_label = ttk.Label(master=options_frame, text="Skill", width=12, anchor="e", justify=tk.LEFT)
        skill_label.grid(row=2, column=0, padx=5)
        v_skill = tk.StringVar()
        om_skill = ttk.OptionMenu(options_frame, v_skill, *skills.skills_dict.keys())
        om_skill.config(width=25)
        om_skill.grid(row=2, column=1)

        affix_label = ttk.Label(master=options_frame, text="Affix", width=12, anchor="e", justify=tk.LEFT)
        affix_label.grid(row=3, column=0, padx=5)
        v_affix = tk.StringVar()
        om_affix = ttk.OptionMenu(options_frame, v_affix, *affixes.affixes_dict.keys())
        om_affix.config(width=25)
        om_affix.grid(row=3, column=1)

        bs_frame = ttk.Frame(master=parent)
        bs_frame.pack(fill=tk.X, padx=4, pady=4)

        bs_title = ttk.Label(master=bs_frame, text="Basic Stats (Offence)", anchor="n", justify=tk.CENTER)
        bs_title.pack(fill=tk.X, side=tk.TOP, pady=2)
        bs_subframe = ttk.Frame(master=bs_frame)
        bs_subframe.pack(fill=tk.X, side=tk.TOP, padx=2, pady=2)

        columns = ("param", "value")

        bs_tree = ttk.Treeview(master=bs_subframe, show="", columns=columns, selectmode="none")
        bs_tree.pack(fill=tk.BOTH)
        bs_tree.column("#1", minwidth=100, width=200, stretch=tk.YES)
        bs_tree.column("#2", minwidth=50, width=50, stretch=tk.NO)

        for x in range(5):
            bs_tree.insert("", tk.END, values=columns)

        btn_frame = ttk.Frame(master=parent)
        btn_frame.pack(fill=tk.X, expand=True, padx=3, pady=5)
        btn_recalculate = tk.Button(master=btn_frame, text="Recalculate", command=self.click)
        btn_recalculate.pack(fill=tk.X, side=tk.LEFT)
        btn_plot = ttk.Button(master=btn_frame, text="Plot", command=self.click)
        btn_plot.pack(fill=tk.X, side=tk.LEFT)

    def cs1(self, parent):

        params = {
            ParamValue(0, "Param1", "Value1"),
            ParamValue(1, "Param2", "Value2")
        }

        cs1_frame = TableFrame(master=parent, title="Overview", items=params, borderwidth=2, relief=tk.RIDGE)
        cs1_frame.pack(fill=tk.X, padx=4, pady=4)

    def cs2(self, parent):

        params = {
            ParamValue(0, "Param1", "Value1"),
            ParamValue(1, "Param2", "Value2")
        }

        cs2_frame = TableFrame(master=parent, title="Hit", items=params, borderwidth=2, relief=tk.RIDGE)
        cs2_frame.pack(fill=tk.X, padx=4, pady=4)

    def cs3(self, parent):

        params = {
            ParamValue(0, "Param1", "Value1"),
            ParamValue(1, "Param2", "Value2")
        }

        cs3_frame = TableFrame(master=parent, title="Ignite", items=params, borderwidth=2, relief=tk.RIDGE)
        cs3_frame.pack(fill=tk.X, padx=4, pady=4)

    def cs4(self, parent):

        params = [
            ParamValue(0, "Param1", "Value1"),
            ParamValue(1, "Param2", "Value2"),
            ParamValue(2, "Param3", "Value3")
        ]

        cs4_frame = TableFrame(master=parent, title="Other", items=params, borderwidth=2, relief=tk.RIDGE)
        cs4_frame.pack(fill=tk.X, padx=4, pady=4)

    def right(self, parent):
        cs_left_frame = ttk.Frame(master=parent, borderwidth=2, relief=tk.RIDGE)
        cs_left_frame.grid(row=0, column=0, sticky=tk.NE)
        #parent.grid_columnconfigure(0, weight=1)
        #parent.grid_rowconfigure(0, weight=1)

        self.cs1(cs_left_frame)
        self.cs2(cs_left_frame)
        self.cs3(cs_left_frame)

        cs_right_frame = ttk.Frame(master=parent, borderwidth=2, relief=tk.RIDGE)
        cs_right_frame.grid(row=0, column=1, sticky=tk.NW)

        self.cs4(cs_right_frame)

    def bottom(self, parent):
        self.text_box = tk.Text(master=parent, state='disabled', height=8,
                           padx=10, pady=10, borderwidth=5, relief=tk.FLAT)
        self.text_box.grid(column=0, row=0, sticky=tk.NSEW)
        ys = ttk.Scrollbar(master=parent, orient='vertical', command=self.text_box.yview())
        ys.grid(column=1, row=0, sticky=tk.NS)
        xs = ttk.Scrollbar(master=parent, orient='horizontal', command=self.text_box.xview())
        xs.grid(column=0, row=1, sticky=tk.EW)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        self.text_box['yscrollcommand'] = ys.set
        self.text_box['xscrollcommand'] = xs.set

    def __init__(self):
        super().__init__()

        self.title("Parameters")
        self.iconbitmap("icon.ico")
        self.style = ttk.Style()
        self.set_theme('default')

        self.columnconfigure(0, weight=1)
        #self.rowconfigure(0, weight=1)
        #self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)

        top_frame = ttk.Frame(master=self, height=20, relief=tk.RAISED, borderwidth=2)
        top_frame.grid(row=0, column=0, sticky="new")
        top_frame.grid_rowconfigure(0, minsize=20)

        self.top(top_frame)

        middle_frame = ttk.Frame(master=self, relief=tk.FLAT, borderwidth=2)
        middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

        left_frame = ttk.Frame(master=middle_frame, relief=tk.GROOVE, borderwidth=2)
        left_frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.left(left_frame)

        right_frame = ttk.Frame(master=middle_frame, relief=tk.GROOVE, borderwidth=2)
        right_frame.grid(row=0, column=1, sticky=tk.NSEW)

        scrollable_frame = ScrollableFrame(master=right_frame, relief=tk.GROOVE, borderwidth=15)
        scrollable_frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.right(scrollable_frame.scrollable_frame)

        bottom_frame = ttk.Frame(master=self, relief=tk.SUNKEN, borderwidth=2)
        bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

        self.bottom(bottom_frame)

        self.logger = Logger(self.text_box)
        sys.stdout = self.logger
        self.logger.writeln("Welcome to EpochProbe v." + self.version.__str__() + "!")


if __name__ == "__main__":
    app = App()
    app.mainloop()

