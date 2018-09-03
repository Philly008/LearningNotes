# -*- coding:utf-8 -*-

# def func(spam):
#     spam[-1]='and' + ' ' + spam[-1]
#     for i in range(len(spam)):
#         print(spam[i], end=',')
#
# spam = ['apple', 'bananas', 'tofu', 'cats', 'dog']
# func(spam)

import copy

def conFun(nameList):
    n = len(nameList)
    newList = copy.copy(nameList)
    newList.insert(n-1, 'and')
    a = str(newList.pop())
    b = str(newList.pop())
    c = ''
    c = b + ' ' + a
    newOne = ''
    newOne = newList[0]
    i = 1
    for j in newList:
        newOne = newOne + ',' + newList[i]
        i = i + 1
        if i == len(newList):
            break
    print(newOne + ',' + c)

if __name__ == '__main__':
    spam = ['apple', 'bananas', 'tofu', 'cats']
    conFun(spam)