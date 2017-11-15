__author__ = 'Philly'

# C:\Users\hasee\Python36\Scripts>pip install openpyxl
# openpyxl 使用说明：http://openpyxl.readthedocs.io/en/default/
from openpyxl import *
# 获得Excel中的测试套件
def getsuit(filename, logger):
    testsuitlis = []
    try:
