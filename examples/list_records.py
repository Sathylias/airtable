#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: list_records.py
Description: Example of retrieving records using Airtable API

Author: Maxime Daraiche <maxime.daraiche@accenture.com>

"""

from airtable.api import AirtableAPI
from config.config import read_yaml

# pylint: disable=missing-function-docstring
def main():

    config = read_yaml("config/env.yaml")
    api_key = config["airtable_api_key"]
    client = AirtableAPI(token=api_key, timeout=60)

    fields = ["Name", "Status"]
    response = client.list_records(config["airtable_base"], "todo_projects", fields)

    print(response.json())


if __name__ == "__main__":
    main()
