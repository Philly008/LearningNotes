# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# chromedriver 放在当前.py 运行的目录下，或者指定绝对路径的chromedriver
#browser = webdriver.Chrome()
browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

for i in range(5000):
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.RETURN)
    htmlElem.send_keys(Keys.DOWN)

print('Done!')