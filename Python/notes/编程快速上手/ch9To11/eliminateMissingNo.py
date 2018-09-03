# -*- coding:utf-8 -*-
# complete the filename that contain sequence like 'spam001.txt', 'spam003.txt'
import os, re, shutil
os.chdir('old')
# 找到指定文件夹中所有带指定前缀的文件
o_filenames = [x for x in os.listdir('.') if  x.startswith('spam')]
print(o_filenames)
#print(os.listdir('.'))

# 定位缺失的编号
numRegex = re.compile(r'^spam(.*?).txt$')
o_num_list = []
for o_filename in o_filenames:
    t_name_re = numRegex.search(o_filename)
    o_num_list.append(t_name_re.group(1))
print(o_num_list)

n_num_list = []
for i in range(1, len(o_num_list) + 1):
    t_i = '%03d' % i
    n_num_list.append(t_i)
print(n_num_list)

for i in n_num_list:
    if i not in o_num_list:
        print('spam%s.txt' % i)

# 对文件改名以消除缺失的编号
for i, v in zip(o_num_list, n_num_list):
    shutil.move('spam%s.txt' % i, 'spam%s.txt' % v)

print('Rename project is done!')
