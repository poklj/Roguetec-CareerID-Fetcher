from os import path
import pathlib
import shelve

import appdirs


class Options:
    appname = "RogueTech_CareerID_fetcher"
    appauthor = "poklj"

    app_path = path.abspath(appdirs.user_data_dir(appname, appauthor))
    settingsPath = path.abspath(app_path + "/settings")
    shelf = None
    isFirst = False

    def __init__(self):
        if not path.exists(self.app_path):
            pathlib.Path(self.app_path).mkdir(parents=True, exist_ok=True)
            self.isFirst = True

        self.shelf = shelve.open(self.settingsPath, writeback=True)
        if self.isFirst:
            self.shelf["bt_installDir"] = pathlib.Path("C:\\Program Files (x86)\\Steam\\steamapps\\common\\BATTLETECH\\")

    def get_log_path(self):
        return path.abspath(self.shelf.get("bt_installDir") + "\Mods\PersistentMapClient\persistent_map_client.log")

    def check_valid_rtInstall(self, v):
        return path.exists(path.abspath(v + "\Mods\PersistentMapClient\persistent_map_client.log"))