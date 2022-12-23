""" Helper to help us to retrieve environments variables and such
"""

import os
import yaml


def load_yaml(yaml_file: str):
    """
    Read data from a yaml file
    :params str yaml_file: Specify the yaml file to be loaded into the environment
    :return: Returns a dictionary containing the yaml data
    """
    with open(os.path.abspath(yaml_file), "r", encoding="utf-8") as yaml_f:
        return yaml.safe_load(yaml_f)
