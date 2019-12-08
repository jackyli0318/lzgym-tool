#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 12:55:32 2018

@author: zhili
"""

'''

'''

# json generator
import json

# generate a json
def json_writer(file_name, tmp_dict, indents=4):
    '''
    json_writer(file_name, tmp_dict)
    file_name -> "xxx.json"
    tmp_dict -> type == dict
    
    ensure_ascii=False is for outputing Chinese characters
    '''
    with open(file_name,"w", encoding='utf-8') as f:
        json.dump(tmp_dict,f, ensure_ascii=False, indent=indents)
        print("Finished writing...")
        
        f.close()


def json2dict(file_name):
    '''
    json_writer(file_name, tmp_dict)
    file_name -> "xxx.json"
    '''
    with open(file_name, 'r', encoding='utf-8') as f:
        
        data = json.load(f)
        
        f.close()
    print("Finished reading...")
    return data