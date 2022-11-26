import os

def fun(my_path):
    if os.path.isfile(my_path):
        print(open(my_path, 'r').read()[-20:])
    if os.path.isdir(my_path):
        extensions = {}
        for entry in os.scandir(my_path):
            extensions[os.path.splitext(entry)[1]] = extensions.get(os.path.splitext(entry)[1], 0) + 1
        print(sorted(extensions.items(), key=lambda x: x[1], reverse=True))
        for entry in os.listdir(my_path):
            if os.path.isdir(os.path.join(my_path, entry)):
                fun(os.path.join(my_path, entry))

fun('D:\\CSSO2022')
