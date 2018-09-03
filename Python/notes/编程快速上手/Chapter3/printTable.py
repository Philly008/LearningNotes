# -*- coding: utf-8 -*-

def printTable(tabledata):
    #创建一个列表，它包含了一些0，数目与tabledata中内层列表的数目相等
    colWidth = [0]*len(tabledata)
    for i in range(len(colWidth)):
        #因为题目假定内存列表都包含同样数目的字符串，所以可以当做是输出的行数
        global num
        num = len(tabledata[i])
        # 用col存储一个列表中的每个字符串长度
        col = []
        for j in range(num):
            col.append(len(tabledata[i][j]))
        # 找出每个列表中的字符串最大长度
        colWidth[i] = max(col[0:int(len(col))])
    # 得到整个列表中字符串的最大长度
    intWidth = max(colWidth[0:len(colWidth)])
    # 输出结果
    for x in range(num):
        for y in range(len(tabledata)):
            print(str(tabledata[y][x]).rjust(intWidth,' '), end = ' ')
        print('\n')

tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

printTable(tableData)