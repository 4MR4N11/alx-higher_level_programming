#!/usr/bin/python3
"""Defines a lookup function"""


def lookup(obj):
    """Return a list of an object's available attributes"""
    return dir(obj)
