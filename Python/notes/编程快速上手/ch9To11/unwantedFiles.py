# -*- coding:utf-8 -*-
# list oversized file in particular folder (and delete it)
import os
for root, dirs, files in os.walk('.'):
    for file in files:
        file_name = os.path.join(root, file)
        if os.path.getsize(file_name) > 1024 * 1024:
            print(file_name)