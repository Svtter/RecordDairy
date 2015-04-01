#!/usr/bin/env python
# coding: UTF-8

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

l = []

for item in config.sections():
    options = config.options(item)
    for option in options:
        print option, ':', config.get(item, option)
