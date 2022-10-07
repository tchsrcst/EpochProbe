from pathlib import Path
import os.path
import json
import re

CHARACTER_CLASS = [
    "Primalist",
    "Mage",
    "Sentinel",
    "Acolyte",
    "Rogue"
]

MASTERY = [
    ["Primalist", "Beastmaster", "Shaman", "Druid"],
    ["Mage", "Sorcerer", "Spellblade", "Runemaster"],
    ["Sentinel", "Void Knight", "Forge Guard", "Paladin", "Forge Guard" ],
    ["Acolyte", "Necromancer", "Lich", "Warlock"],
    ["Rogue", "Bladedancer", "Marksman", "Falconer"]
]

CONTAINER = dict([
    (1, "Inventory"),
    (2, "Helmet"),
    (3, "Body Armor"),
    (4, "Weapon"),
    (5, "Off hand"),
    (6, "Gloves"),
    (7, "Belt"),
    (8, "Boots"),
    (9, "Ring 1"),
    (10, "Ring 2"),
    (11, "Amulet"),
    (12, "Relic"),
    (24, "Blessing"),
    (25, "Blessing"),
    (29, "Idol"),
    (32, "IdolSpace"),
    (33, "Blessing"),
    (34, "Blessing"),
    (35, "Blessing")
])


class ItemData:

    def __init__(self, container_id, inventory_pos, data):
        self.container = CONTAINER[container_id]
        self.inventory_pos = inventory_pos
        self.data = data

    def __str__(self):
        return "[{}] pos={}".format(
            self.container,
            self.inventory_pos,
        )


class SaveData:

    def __init__(self, filename, filepath, slot, character_name, level, hardcore, character_class, mastery, data):
        self.filename = filename
        self.filepath = filepath
        self.slot = slot
        self.character_name = character_name
        self.level = level
        self.hardcore = hardcore
        self.character_class = character_class
        self.mastery = mastery
        self.data = data

    def __str__(self):
        return "[{}] {} lvl: {}{}".format(
            self.mastery, self.character_name, self.level, " [HC]" if self.hardcore else ""
        )


class SaveManager:
    EPOCH = "EPOCH"
    REL_PATH = "AppData\\LocalLow\\Eleventh Hour Games\\Last Epoch\\Saves"
    SLOT_PATTERN = '1CHARACTERSLOT.*\\d+$'

    def __init__(self):
        self.home = str(Path.home())
        self.path = os.path.join(self.home, SaveManager.REL_PATH)
        print("[SaveManager] Local saves path: " + self.path)
        print("[SaveManager] Scanning...")
        filenames = os.listdir(self.path)

        slot_names = []
        for filename in filenames:
            if re.match(SaveManager.SLOT_PATTERN, filename):
                slot_names.append(filename)

        print("[SaveManager] Found: " + slot_names.__str__())

        i = 0
        self.saves = []

        print("[SaveManager] Characters: ")
        for filename in slot_names:
            filepath = os.path.join(self.path, filename)
            d = SaveManager.load(filepath)
            save = SaveData(
                filename, filepath,
                d['slot'], d['characterName'], d['level'], d['hardcore'],
                CHARACTER_CLASS[d['characterClass']],
                MASTERY[d['characterClass']][d['chosenMastery']],
                d
            )
            print("{}: {}".format(i, save))
            self.saves.append(save)
            i += 1


    @staticmethod
    def load(filepath):
        file = open(filepath)
        content = file.read()
        file.close()
        d = json.loads(content.replace(SaveManager.EPOCH, ""))
        return d

    @staticmethod
    def equipped_items(save):
        items = []
        print("-"*80)
        print(save.__str__())
        i = 0
        for item in save.data['savedItems']:
            item_data = ItemData(item['containerID'], item['inventoryPosition'], item['data'])
            print("{}: {}".format(i, item_data))
            items.append(item_data)
            i += 1

        return items


if __name__ == "__main__":
    sm = SaveManager()
    s = sm.saves[4]
    SaveManager.equipped_items(s)

