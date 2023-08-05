from configparser import ConfigParser
from json import dumps


class ConfigHandler:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('config.ini')

    def get(self, section, key):
        return self.config[section][key]

    def get_int(self, section, key):
        return int(self.config[section][key])

    def get_float(self, section, key):
        return float(self.config[section][key])

    def get_bool(self, section, key):
        return self.config[section].getboolean(key)

    def get_list(self, section, key):
        return self.config[section][key].split(',')

    def check_any_empty(self, section, keys):
        for key in keys:
            if self.config[section][key] == '':
                return True
        return False

    def check_any_empty(self):
        for section in self.config.sections():
            for key in self.config[section]:
                if self.config[section][key] is None or self.config[section][key] == '':
                    return True
        return False

    def __str__(self):
        out_dict = {}
        for section in self.config.sections():
            out_dict[section] = {}
            for key in self.config[section]:
                out_dict[section][key] = self.config[section][key]
        return dumps(out_dict, indent=4)

