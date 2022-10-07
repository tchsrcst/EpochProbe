import http
import json
from http import client


class LastEpochToolsManager:
    base_url = 'www.lastepochtools.com'
    data_url = '/planner/js/data.js'
    itemdb_url = '/db/js/itemdb.js'
    coredb_url = '/db/js/coredb.js'

    def __init__(self):
        # content = self.get(LastEpochToolsManager.coredb_url)
        #content = self.get(LastEpochToolsManager.itemdb_url)
        #content = self.get(LastEpochToolsManager.data_url)
        # self.parse_coredb(content)
        pass

    @staticmethod
    def get(url):
        print('GET ' + url)
        connection = http.client.HTTPSConnection(LastEpochToolsManager.base_url)
        connection.request("GET", url)
        response = connection.getresponse()
        print("HTTP {} {}".format(response.status, response.reason))
        content = ""
        if response.status == 200:
            content = response.read().decode()
            print(content)
        connection.close()
        return content

    @staticmethod
    def parse_coredb(content):
        content = content.replace("window.coreDB=", "")
        print(type(content))
        json_object = json.loads(content)
        for p in json_object.propertyList:
            print(p.propertyName)
