# Saves and loads pieces of text to the clipboard.
'''
Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
        py.exe mcb.pyw list  - Loads all keywords to clipboard.
'''
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# 第 2 步：用一个关键字保存剪贴板内容
# Save clipboard content.
if len(sys.argv) == 3 :
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # 列出关键字和加载关键字的内容
    # List keywords and load content:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

mcbShelf.close()