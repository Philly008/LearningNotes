Q1：只是 import urllib   ,python错误 module 'urllib' has no attribute 'request'
A1：因为python3.X有时候不会将子模块自动导入进去，所以改成import url.request问题就解决了

Q2: python3中已取消 urllib2
A2:
a new urllib package was created. It consists of code from
urllib, urllib2, urlparse, and robotparser. The old
modules have all been removed. The new package has five submodules:
urllib.parse, urllib.request, urllib.response,
urllib.error, and urllib.robotparser. The
urllib.request.urlopen() function uses the url opener from
urllib2.

Q3:
A3: http://httpstat.us/500 该网址会始终返回 500 错误码

Q4: cannot use a string pattern on a bytes-like object
Q5: html = html.decode('utf-8') # python3 需要加上这句






