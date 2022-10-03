import os.path
import glob
import re


class SaveManager:
    abs_path = "C:\\Users\\Max\\AppData\\LocalLow\\Eleventh Hour Games\\Last Epoch\\Saves"
    pattern = '1CHARACTERSLOT.*\\d+$'
    paths_arr = []
    filenames = []

    def __init__(self):
        filenames = os.listdir(self.abs_path)
        for filename in filenames:
            if re.match(self.pattern, filename):
                self.filenames.append(filename)
                print(filename)

    def load(self, save_name):
        filepath = os.path.join(self.abs_path, save_name)
        file = open(filepath)
        file.close()

