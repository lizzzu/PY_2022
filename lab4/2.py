import os

def fun(directory, file):
    with open(file, 'a') as f:
        for entry in os.scandir(directory):
            if entry.is_file() and entry.name.startswith('A'):
                f.write(entry.path + '\n')

fun('D:\\', 'D:\\fisier.txt')
