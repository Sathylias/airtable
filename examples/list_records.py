#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: list_records.py
Description: Example of retrieving records using Airtable API

Author: Maxime Daraiche <max@techstew.dev>

"""

from airtable.api import AirtableAPI
from airtable.config.utils import load_yaml

# pylint: disable=missing-function-docstring
def main():

    config = load_yaml("env.yaml")
    client = AirtableAPI(token=config["airtable_api_key"], timeout=60)

    response = client.list_records(
        config["airtable_base"], "todo_projects", ["Name", "Status"]
    )

    print(response.json())


if __name__ == "__main__":
    main()
