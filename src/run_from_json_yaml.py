"""
@Author George Shen
@Title run_from_json_yaml
@Version 1
"""

import json
import yaml
import os


def open_org_path():
    path = input("What is the path of the file: ")
    try:
        path = os.path.abspath(path)
        if os.path.exists(path):
            if path.endswith('.yaml'):
                print("Yaml file found:\n")
                with open(path,'r+') as yaml:
                    pass

            elif path.endswith('.json'):
                print("JSON file found:\n")
                with open(path, 'r+') as json:
                    pass
            else:
                print("File is not a yaml or json")
                return False
        else:
            print("This path does not exist")
            return False
    except:
        print("Not a proper path")
        return False

if __name__ == '__main__':
    i=0
    try_limit = 3
    while (i < try_limit):
        status = open_org_path()
        if status == False:
            i += 1
        else:
            break