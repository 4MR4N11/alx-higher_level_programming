#!/usr/bin/python3
"""Create an object from a JSON file module"""
import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'"""
    with open(filename, "r") as file:
        return json.load(file)
