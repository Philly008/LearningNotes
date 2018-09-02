__author__ = 'Philly'
#coding:utf-8
from selenium import webdriver
import logging.config

# 通过配置文件来增加log
logging.config.fileConfig(r"E:\workspace\PGauto\com\log.conf", disable_existing_loggers=False)
logger = logging.getLogger("performtest")

# 获得测试套件内容
testsuitfilename = "E:/workspace/PGauto/data/testcase.xlsx"
testsuitlist = getexcel.getsuit()
