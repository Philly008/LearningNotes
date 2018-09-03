# coding:utf-8
# 疯狂填词
# import re
#
# # 读取文本
# file = open('a.txt', 'r')
# words = file.read()
# file.close()
# # 查找关键字
# pattern = re.compile('ADJECTIVE|NOUN|VERB|ADVERB')
# mo = pattern.findall(words)
# # 依次替换每一个关键字
# for word in mo:
#     rep1 = input(f'Enter a {word}:\n> ')
#     regex = re.compile(word)
#     words = regex.sub(rep1, words, 1)
# print(words)
# # 替换后的文本写入新的文件
# new_file = open('b.txt', 'w')
# new_file.write(words)
# new_file.close()

import re
text = 'The ADJECTIVE panda walked to the NOUN and the VERB. A nearby NOUN was unaffected by these events.'
repWordList = re.compile(r'[A-Z]{2,}').findall(text)
repList = []
for wordString in repWordList:
    if wordString[0].lower() == 'a':
        rep = input('Enter an %s\n' % wordString).lower()
    else:
        rep = input('Enter a %s\n' % wordString).lower()
    text = text.replace(wordString, rep, 1)
print(text)
open(r'.\b.txt', 'w').write(text)