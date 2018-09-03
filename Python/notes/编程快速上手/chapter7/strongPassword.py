# coding:utf-8
'''
测试数据：uusssZZmMMiiOO22 复制到剪贴板
'''
import pyperclip, re

text = str(pyperclip.paste())
def detection(text):
    if len(text) <=8:
        return False
    number = re.compile(r'\d+')
    if number.search(text) == None:
        return False
    number2 = re.compile(r'[A-Z]+')
    if number2.search(text) == None:
        return False
    number3 = re.compile(r'[a-z]+')
    if number3.search(text) == None:
        return False
    return True

if __name__ == '__main__':
    a = detection(text)
    print(a)