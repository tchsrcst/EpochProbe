import tkinter as tk


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
