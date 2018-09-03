# -*- coding:utf-8 -*-
import os, shutil

#print(os.getcwd())
#os.makedirs('old')
os.chdir('old')
#print(os.getcwd())
# to generate a file, and make sure the file has not existed
try:
    os.makedirs('copy_to_this_dir')
except FileExistsError:
    pass
# walk through a dir and find particular file, like '.pdf', '.txt', etc.
for root, dirs, files in os.walk('.'):
    for file in files:
        # what kind of file that you want to copy
        if file.endswith('.py') or file.endswith('.bak'):
            if file not in os.listdir('copy_to_this_dir'):
                # copy these files to a new folder
                shutil.copy(os.path.join(root, file), 'copy_to_this_dir')
                print('Done.')
