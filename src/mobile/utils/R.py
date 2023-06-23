import configparser
import os
from enum import Enum


class R(Enum):
    # use relative path to configuration files
    TESTDATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'resources', '__testdata.ini')
    DRIVER_CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'resources', '__config.ini')

    def read_config_value(self, section, key):
        # Retrieve the config file path from the TESTDATA value
        filepath = self.value

        # Create an instance of the configparser
        config = configparser.ConfigParser()

        # Read the config file
        config.read(filepath)

        # Check if the section and key exist in the config file
        if config.has_section(section) and config.has_option(section, key):
            value = config.get(section, key)
            return value

        return None
