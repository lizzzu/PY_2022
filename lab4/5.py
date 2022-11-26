import os

def fun(target, to_search):
    if not os.path.isfile(target) and not os.path.isdir(target):
        raise ValueError('Wrong file type: ' + target)
    if os.path.isfile(target):
        if to_search in open(target).read():
            print(target)
    else:
        for entry in os.listdir(target):
            fun(os.path.join(target, entry), to_search)

try: fun('C:\\Facultate', '5')
except Exception as e: print(e)
