import openpyxl
import os

txtfiles = []   # 找到但钱目录所有的txt文件
for txt in os.listdir('.'):
    if txt.endswith('.txt'):
        txtfiles.append(txt)

wb = openpyxl.Workbook()
sheet = wb.active

j = 1
for file in txtfiles:
    txt = open(file, 'r')
    i = 1   # 第二列从第一行重新开始
    for line in txt.readlines():
        sheet.cell(row = i, column = j).value = line
        i += 1
    j += 1

wb.save('文本文件到表格.xlsx')