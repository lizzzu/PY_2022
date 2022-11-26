import os

def fun(directory):
    return sorted(set([os.path.splitext(entry.name)[1][1:] for entry in os.scandir(directory) if entry.is_file()]))

print(fun('D:\\'))
