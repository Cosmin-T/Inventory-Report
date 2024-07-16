# config_ini.py

import configparser

INI = '/Volumes/Samsung 970 EVO/Documents/Python/aga_inventory_report/logic/config.ini'
def con():
    config = configparser.ConfigParser()
    config.read(INI)
    return config