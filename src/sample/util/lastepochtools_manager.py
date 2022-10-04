import http


class LastEpochToolsManager:
    base_url = 'https://www.lastepochtools.com'
    data_url = base_url + '/planner/js/data.js'
    itemdb_url = base_url + '/db/js/itemdb.js'
    coredb_url = base_url + '/db/js/coredb.js'

    def __init__(self):
        print(self.base_url)

    def load(self, save_name):
        print(self.base_url)

