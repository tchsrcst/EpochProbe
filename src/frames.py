import sys
import tkinter as tk
import tkinter.ttk as ttk

from core.data import scenarios, skills, affixes
from core.data.stats import ParamValue, values
import context as cntx
from templates import TableFrame, ScrollableFrame, Logger


class TopFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.grid(row=0, column=0, sticky=tk.NSEW)

        btn_1 = ttk.Button(master=self, text="btn1", width=8)
        btn_1.grid(row=0, column=0, sticky=tk.N)
        btn_2 = ttk.Button(master=self, text="btn2", width=8)
        btn_2.grid(row=0, column=1, sticky=tk.N)

        v_character_slot = tk.StringVar()
        v_character_slot.set('CharacterSlot')
        om_character_slot = ttk.OptionMenu(self, v_character_slot, *cntx.sm.saves)
        om_character_slot.config(width=25)
        om_character_slot.grid(row=0, column=2, sticky=tk.N)

        v_gui_theme = tk.StringVar()
        om_gui_theme = ttk.OptionMenu(self, v_gui_theme, *cntx.style.theme_names(), command=cntx.style.theme_use)
        v_gui_theme.set('default')
        om_gui_theme.config(width=6)
        om_gui_theme.grid(row=0, column=3, sticky=tk.NE)


class MiddleFrame(ttk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.grid(row=1, column=0, sticky=tk.NSEW)
        self.rowconfigure(0, weight=1)

        left_frame = LeftFrame(master=self, relief=tk.RAISED, borderwidth=2)
        left_frame.grid(row=0, column=0, sticky=tk.NSEW)

        right_frame = RightFrame(master=self, relief=tk.FLAT, borderwidth=2)
        right_frame.grid(row=0, column=1, sticky=tk.N)


class BottomFrame(ttk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.grid(row=2, column=0, sticky=tk.NSEW)

        text_box = tk.Text(master=self, state='disabled', height=8,
                                padx=10, pady=10, borderwidth=5, relief=tk.FLAT)
        text_box.grid(column=0, row=0, sticky=tk.NSEW)
        ys = ttk.Scrollbar(master=self, orient='vertical', command=text_box.yview())
        ys.grid(column=1, row=0, sticky=tk.NS)
        xs = ttk.Scrollbar(master=self, orient='horizontal', command=text_box.xview())
        xs.grid(column=0, row=1, sticky=tk.EW)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        text_box['yscrollcommand'] = ys.set
        text_box['xscrollcommand'] = xs.set

        cntx.logger = Logger(text_box)
        sys.stdout = cntx.logger
        cntx.logger.writeln("Welcome to EpochProbe v." + cntx.app_version + "!")


class LeftFrame(ttk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        options_frame = OptionsFrame(self, borderwidth=2, relief=tk.RIDGE)
        options_frame.grid(row=0, column=0, sticky=tk.NSEW)

        bs_frame = BasicStatsFrame(master=self)
        bs_frame.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NSEW)

        controls_frame = ControlsFrame(master=self, borderwidth=2, relief=tk.RIDGE)
        controls_frame.grid(row=2, column=0, sticky=tk.NSEW)


class RightFrame(ttk.Frame):

    def cs(self, parent):

        params = {
            ParamValue(0, "Param1", "Value1"),
            ParamValue(1, "Param2", "Value2")
        }

        cs1_frame = TableFrame(master=parent, title="Overview", items=params, borderwidth=2, relief=tk.RIDGE)
        cs1_frame.pack(padx=4, pady=4)

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        scrollable_frame = ScrollableFrame(master=self, relief=tk.FLAT, borderwidth=2)
        scrollable_frame.grid(row=0, column=0, sticky=tk.N)

        cs_left_frame = ttk.Frame(master=scrollable_frame.sub_frame, borderwidth=2, relief=tk.RIDGE)
        cs_left_frame.grid(row=0, column=0, sticky=tk.NE)

        self.cs(cs_left_frame)
        self.cs(cs_left_frame)
        self.cs(cs_left_frame)

        cs_right_frame = ttk.Frame(master=scrollable_frame.sub_frame, borderwidth=2, relief=tk.RIDGE)
        cs_right_frame.grid(row=0, column=1, sticky=tk.NW)

        self.cs(cs_right_frame)


class OptionsFrame(ttk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        lbl_scenario = ttk.Label(master=self, text="Scenario", width=12, anchor="e", justify=tk.LEFT)
        lbl_scenario.grid(row=0, column=0, padx=5)
        v_scenario = tk.StringVar()
        om_scenario = ttk.OptionMenu(self, v_scenario, *scenarios.scenarios_dict)
        om_scenario.config(width=25)
        om_scenario.grid(row=0, column=1)

        lbl_skill = ttk.Label(master=self, text="Skill", width=12, anchor="e", justify=tk.LEFT)
        lbl_skill.grid(row=1, column=0, padx=5)
        v_skill = tk.StringVar()
        om_skill = ttk.OptionMenu(self, v_skill, *skills.skills_dict.keys())
        om_skill.config(width=25)
        om_skill.grid(row=1, column=1)

        lbl_affix = ttk.Label(master=self, text="Affix", width=12, anchor="e", justify=tk.LEFT)
        lbl_affix.grid(row=2, column=0, padx=5)
        v_affix = tk.StringVar()
        om_affix = ttk.OptionMenu(self, v_affix, *affixes.affixes_dict.keys())
        om_affix.config(width=25)
        om_affix.grid(row=2, column=1)


class BasicStatsFrame(ttk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        bs_title = ttk.Label(master=self, text="Basic Stats", anchor="n", justify=tk.CENTER)
        bs_title.grid(row=0, column=0, sticky=tk.N)

        columns = ("param", "value")

        sub_frame = ttk.Frame(master=self, borderwidth=2, relief=tk.RIDGE)
        sub_frame.grid(row=1, column=0, sticky=tk.NSEW)
        sub_frame.columnconfigure(0, weight=1)
        sub_frame.columnconfigure(1, weight=0)
        sub_frame.rowconfigure(0, weight=1)

        bs_tree = ttk.Treeview(master=sub_frame, show="", columns=columns, selectmode="none")
        bs_tree.grid(row=0, column=0, sticky=tk.NSEW)
        bs_tree.column("#1", minwidth=100, width=200, stretch=tk.YES)
        bs_tree.column("#2", minwidth=50, width=50, stretch=tk.NO)

        for x in range(8):
            bs_tree.insert("", tk.END, values=values[x].get())

        ys = ttk.Scrollbar(master=sub_frame, orient=tk.VERTICAL, command=bs_tree.yview())
        ys.grid(row=0, column=1, sticky=tk.NS)
        bs_tree['yscrollcommand'] = ys.set


class ControlsFrame(ttk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        btn_recalculate = tk.Button(master=self, text="Recalculate", command=self.click)
        btn_recalculate.grid(row=0, column=0)
        btn_plot = ttk.Button(master=self, text="Plot", command=self.click)
        btn_plot.grid(row=0, column=1)
        btn_plot2 = ttk.Button(master=self, text="Plot2", command=self.click)
        btn_plot2.grid(row=0, column=3)

    def click(self):
        pass

