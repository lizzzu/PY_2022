import os
from pprint import pprint

def fun(dir_path):
    return [os.path.join(dir_path, entry) for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]

pprint(fun('C:\\Facultate\\CSSO\\Laboratoare\\Week1\\Rezultate'))
