# -*- coding:utf-8 -*-
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.
import shutil, os, re

# 第 1 步：为美国风格的日期创建一个正则表达式
# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)  # all text before the date
    ((0|1)?\d)- # one or two digits for the month
    ((0|1|2|3)?\d)- # one or two digits for the day
    ((19|20)\d\d)   # four digits for the year
    (.*?)$  # all text after the date    
    """, re.VERBOSE)

# 第 2 步：识别文件名中的日期部分
# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo == None:
        continue
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # 第 3 步：构成新文件名，并对文件改名
    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # Get the full, absolute file path.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename the files.
    print('Rename "%s" to "%s" ...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename) # uncomment after testing