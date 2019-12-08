LZ & GYM's Python Tool

Author: LZ & GYM

# Example Package

This is a simple example about how to use lzgym's tool:

from lzgym-tool import json2dict, json_writer

# convert a json into a dictionary
lz_dict = json2dict("example.json")

# write a dictionary into a json
json_writer("example.json", lz_dict)


# More info about the methods:
help(json2dict)

help(json_writer)
