from configparser import ConfigParser


CONFIG_FILE = './config.ini'



parser = ConfigParser()
parser.read(CONFIG_FILE)

config = dict()

for section in parser.sections():
    config[section] = dict()

    for key, value in parser.items(section):
        config[section][key] = value
