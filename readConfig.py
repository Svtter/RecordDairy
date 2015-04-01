#!/usr/bin/env python
# coding: UTF-8

import ConfigParser

config = ConfigParser.ConfigParser()
filename = raw_input("Input file name:")
config.read(filename)

print config.get("global", "ip")
