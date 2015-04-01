#!/usr/bin/env python
# coding: UTF-8

import ConfigParser
from Show import Item

config = ConfigParser.ConfigParser()
config.read('config.ini')

l = []

for item in config.sections():
    options = config.options(item)
    temp = Item()
    for option in options:
        # print option, ':', config.get(item, option)
        setattr(temp, option, config.get(item, option))
    l.append(temp)

for x in l:
    x.showStatus()
