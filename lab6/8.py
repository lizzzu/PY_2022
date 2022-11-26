import os
import re

def fun(path, regex):
    for root, _, files in os.walk(path):
        for file in files:
            filename = re.match(regex, file)
            content = re.search(regex, open(os.path.join(root, file), 'r').read())
            if filename and content: print('>>', file)
            elif filename or content: print(file)

fun('D:\\New', r'\w{2}\.\w{3}')
