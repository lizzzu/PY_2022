import os

def fun(target, to_search, callback):
    if not os.path.isfile(target) and not os.path.isdir(target):
        callback(ValueError('Wrong file type: ' + target))
    try:
        if os.path.isfile(target):
            if to_search in open(target).read():
                print(target)
        else:
            for entry in os.listdir(target):
                fun(os.path.join(target, entry), to_search, callback)
    except Exception as e:
        callback(e)

fun('C:\\Facultate\\A', '5', lambda e: print(f'Error: {e}'))
