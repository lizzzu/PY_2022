import os

def fun(file):
    return {
        'full_path': os.path.abspath(file),
        'file_size': os.path.getsize(file),
        'file_extension': os.path.splitext(file)[1][1:],
        'can_read': os.access(file, os.R_OK),
        'can_write': os.access(file, os.W_OK)
    }

print(fun('D:\\ok.txt'))
