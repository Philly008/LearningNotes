# -*- coding:utf-8 -*-
# lucky.py - Opens several Google search results.
import requests, sys, webbrowser, bs4

# 第 1 步：获取命令行参数，并请求查找页面
print('Googling ...')   # display text while downloading the Google  page
res = requests.get('https://www.baidu.com/s?wd=' + ''.join(sys.argv[1:]))
#res.raise_for_status()
if res.status_code != 200:
    print('requests fail')
# 第 2 步：找到所有的结果
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
# Open a browser tab for each result.
linkElems = soup.select('.t a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://www.baidu.com/' + linkElems[i].get('href'))

