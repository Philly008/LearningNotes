# coding:utf-8
import re, os
path = '.'
fileNameList = os.listdir(path)
for fileNameString in fileNameList:
    mo = re.compile(r'.+\.txt$').search(fileNameString)
    if mo == None:
        continue
    else:
        txtFileString = open(os.path.join(path, mo.group())).read()
        # 匹配正则表达式
        resultList = re.compile(r'\d{3}').findall(txtFileString)
        print('\n'.join(resultList))