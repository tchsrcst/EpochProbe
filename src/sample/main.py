import tkinter as tk
from tkinter import Tk, font
import tkinter.ttk as ttk
import sys

from util import save_manager

import input
import plot
from skill import skills
from affix import affixes
from scenario import scenarios


class App(Tk):
    skill = skills.Fireball
    scenario = scenarios.BasicScenario
    base = input.InputBase
    input = base
    logger = None
    style = None
    selected_theme = None

    fg_color = "#616975"
    bg_color = "#2b2b2b"
    pn_color1 = "#313335"
    pn_color2 = "#3c3f41"

    font = ()

    bs_array = [
        (0, "increased Cast Speed", "0.0"),
        (1, "Increased Damage", "0.0"),
        (2, "Increased Spell Damage", "0.0"),
        (3, "Increased Elemental Damage", "0.0"),
        (4, "Increased Elemental Damage over Time", "0.0"),
        (5, "Increased Fire Damage", "0.0"),
        (6, "Increased Damage over Time", "0.0"),
        (7, "Increased Ignite Chance", "0.0"),
        (8, "Increased Ignite Duration", "0.0"),
        (9, "Increased Crit Chance", "0.0"),
        (10, "Increased Crit Multiplier", "0.0"),
        (11, "Fire Penetration", "0.0"),
        (12, "Total More Damage", "0.0")
    ]

    bs_entry_array = []

    cs_array = [
        (0, "Total Hit Increased Damage", "0.0"),
        (1, "Total_Dot_increased Damage", "0.0"),
        (2, "Regular Hit Damage", "0.0"),
        (3, "Effective Critical_Strike Chance", "0.0"),
        (4, "Effective Critical Strike Multiplier", "0.0"),
        (5, "Effective Critical Strike Modifier", "0.0"),
        (6, "Critical Hit Damage", "0.0"),
        (7, "Effective Hit Damage", "0.0"),
        (8, "Effective Ignite Chance", "0.0"),
        (9, "Effective Ignite Duration", "0.0"),
        (10, "Effective Ignite Damage", "0.0"),
        (11, "Effective Ignite DPS", "0.0"),
        (12, "Effective Cast Speed", "0.0"),
        (13, "Effective Hit DPS", "0.0"),
        (14, "Effective Ignite DPS", "0.0"),
        (15, "Effective Combined DPS", "0.0")
    ]

    cs_entry_array = []

    def get_params(self):
        input.inc_cast_speed = float(self.bs_entry_array[0].get())
        input.inc_damage = float(self.bs_entry_array[1].get())
        input.inc_spell_damage = float(self.bs_entry_array[2].get())
        input.inc_elemental_damage = float(self.bs_entry_array[3].get())
        input.inc_elemental_dot = float(self.bs_entry_array[4].get())
        input.inc_fire_damage = float(self.bs_entry_array[5].get())
        input.inc_dot = float(self.bs_entry_array[6].get())
        input.inc_ignite_chance = float(self.bs_entry_array[7].get())
        input.inc_ignite_duration = float(self.bs_entry_array[8].get())
        input.inc_crit_chance = float(self.bs_entry_array[9].get())
        input.inc_crit_multiplier = float(self.bs_entry_array[10].get())
        input.fire_penetration = float(self.bs_entry_array[11].get())
        input.total_more_damage = float(self.bs_entry_array[12].get())
        return input

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())

    def click(self):
        self.input = self.get_params()
        plot.main(self.skill, self.input, self.scenario)

    def __init__(self):
        super().__init__()

        # 16x9
        self.geometry("1280x720")
        self.title("Parameters")

        self.style = ttk.Style(self)
        # winnative clam alt default classic vista xpnative
        self.style.theme_names()
        self.style.theme_use('clam')
        current_theme = self.style.theme_use()

        self.font = tk.font.nametofont("TkDefaultFont")
        self.font.configure(family='JetBrains Mono', size=12, weight=font.NORMAL)

        # ----- TOP FRAME -----
        top_frame = tk.Frame(self, background=self.pn_color2)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        """
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(top_frame, text='Themes')
        theme_frame.pack()

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                width=10,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme)
            rb.pack(expand=True, fill=tk.X)
        """

        sm = save_manager.SaveManager()

        save_frame = tk.Frame(master=top_frame)

        # label = tk.Label(master=save_frame, anchor='w', text='CharacterSlot', width=15, height=2)
        # label.pack(side=tk.LEFT)
        v_save = tk.StringVar()
        om_save = tk.OptionMenu(save_frame, v_save, *sm.filenames)
        v_save.set('CharacterSlot')
        om_save.config(width=30)
        om_save.pack(side=tk.LEFT)
        save_frame.grid(row=0, column=0)

        scenario_frame = tk.Frame(master=top_frame)
        # label = tk.Label(master=scenario_frame, anchor='w', text='Scenario', width=15, height=2)
        # label.pack(side=tk.LEFT)
        v_scenario = tk.StringVar()
        om_scenario = tk.OptionMenu(scenario_frame, v_scenario, *scenarios.scenarios_dict.keys())
        v_scenario.set('Scenario')
        om_scenario.config(width=20)
        om_scenario.pack(side=tk.LEFT)
        scenario_frame.grid(row=0, column=1)

        skill_frame = tk.Frame(master=top_frame)
        # label = tk.Label(master=skill_frame, anchor='w', text='Skill', width=15, height=2)
        # label.pack(side=tk.LEFT)
        v_skill = tk.StringVar()
        om_skill = tk.OptionMenu(skill_frame, v_skill, *skills.skills_dict.keys())
        v_skill.set('Skill')
        om_skill.config(width=20)
        om_skill.pack(side=tk.LEFT)
        skill_frame.grid(row=0, column=2)

        affix_frame = tk.Frame(master=top_frame)
        v_affix = tk.StringVar()
        om_affix = tk.OptionMenu(skill_frame, v_affix, *affixes.affixes_dict.keys())
        v_skill.set('Skill')
        om_affix.config(width=20)
        om_affix.pack(side=tk.LEFT)
        affix_frame.grid(row=0, column=3)

        # ----- MIDDLE FRAME -----
        middle_frame = tk.Frame(self, background=self.pn_color1)
        middle_frame.pack(fill=tk.BOTH)

        left_frame = tk.Frame(middle_frame, background=self.pn_color1)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        right_frame = tk.Frame(middle_frame, background=self.pn_color1)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        title2 = tk.Label(master=left_frame, text="Basic Stats (Offence)")
        title2.pack(fill=tk.X)

        bs_frame = tk.Frame(master=left_frame)
        for x in range(len(self.bs_array)):
            bs_subframe = tk.Frame(master=bs_frame, relief=tk.RAISED, borderwidth=0)
            bs_entry1_text = tk.StringVar()
            bs_entry1 = tk.Entry(master=bs_subframe, textvariable=bs_entry1_text, width=30, bg="white")
            bs_entry1_text.set(self.bs_array[x][1])
            bs_entry1.pack(side=tk.LEFT)
            bs_entry2_text = tk.StringVar()
            bs_entry2 = tk.Entry(master=bs_subframe, textvariable=bs_entry2_text, width=5, bg="white")
            bs_entry2_text.set(self.bs_array[x][2])
            bs_entry2.pack(side=tk.LEFT)
            self.bs_entry_array.append(bs_entry2)
            bs_subframe.pack()
        bs_frame.pack()

        btn_frame = tk.Frame(master=left_frame)
        button1 = tk.Button(master=btn_frame, text="Calculate", command=self.click)
        button1.pack(fill=tk.X)

        button2 = tk.Button(master=btn_frame, text="Button2", command=self.click)
        button2.pack(fill=tk.X)

        button3 = tk.Button(master=btn_frame, text="Button3", command=self.click)
        button3.pack(fill=tk.X)

        btn_frame.pack(fill=tk.X)

        title3 = tk.Label(master=right_frame, text="Calculated Stats (Offence)")
        title3.pack(fill=tk.X)

        cs_frame = tk.Frame(master=right_frame)
        for x in range(len(self.cs_array)):
            cs_subframe = tk.Frame(master=cs_frame, relief=tk.RAISED, borderwidth=0)
            cs_entry1_text = tk.StringVar()
            cs_entry1 = tk.Entry(master=cs_subframe, textvariable=cs_entry1_text, width=30, bg="white")
            cs_entry1_text.set(self.cs_array[x][1])
            cs_entry1.pack(side=tk.LEFT)
            cs_entry2_text = tk.StringVar()
            cs_entry2 = tk.Entry(master=cs_subframe, textvariable=cs_entry2_text, width=5, bg="white")
            cs_entry2_text.set(self.cs_array[x][2])
            cs_entry2.pack(side=tk.LEFT)
            self.cs_entry_array.append(cs_entry2)
            cs_subframe.pack()
        cs_frame.pack()

        # ----- BOTTOM FRAME -----
        bottom_frame = tk.Frame(master=self, background=self.pn_color1)
        text_box = tk.Text(master=bottom_frame, state='disabled', width=120, height=10,
                           foreground=self.fg_color, background=self.bg_color,
                           padx=10, pady=10, borderwidth=5, relief=tk.FLAT)
        ys = tk.Scrollbar(master=bottom_frame, orient='vertical', command=text_box.yview())
        xs = tk.Scrollbar(master=bottom_frame, orient='horizontal', command=text_box.xview())
        text_box['yscrollcommand'] = ys.set
        text_box['xscrollcommand'] = xs.set
        text_box.grid(column=0, row=0, sticky='nwes')
        xs.grid(column=0, row=1, sticky='we')
        ys.grid(column=1, row=0, sticky='ns')
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_rowconfigure(0, weight=1)
        bottom_frame.pack(fill=tk.X)

        self.logger = Logger(text_box)
        sys.stdout = self.logger

        self.logger.writeln("available tkinter themes: " + self.style.theme_names().__str__())
        self.logger.writeln("current tkinter theme: " + current_theme)



if __name__ == "__main__":
    app = App()
    app.mainloop()

