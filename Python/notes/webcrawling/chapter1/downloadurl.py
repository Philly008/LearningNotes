# coding=utf-8
import urllib.request
import urllib.error
import re
import itertools
from urllib.parse import urlparse,urljoin

# 下载网页，该函数能够捕获异常、重试下载并设置用户代理
def download(url, user_agent='wswp', num_retries=2):
    print('Downloading: ', url)
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        '''
        a new urllib package was created. It consists of code from  
urllib, urllib2, urlparse, and robotparser. The old  
modules have all been removed. The new package has five submodules:  
urllib.parse, urllib.request, urllib.response,  
urllib.error, and urllib.robotparser. The  
urllib.request.urlopen() function uses the url opener from  
urllib2.
        '''
        html = urllib.request.urlopen(request).read()
        html = html.decode('utf-8')
    except urllib.error.URLError as e:
        print('Download error: ', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries-1)
    return html

# 网站地图爬虫
def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here

# ID 遍历爬虫
def crawl_sitema_by_id():
    # maximum number of consecutive download errors allowed
    max_errors = 5
    # current number of consecutive download errors
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d' % page
        html = download(url)
        if html is None:
            # reveived an error trying to download this webpage
            num_errors += 1
            if num_errors == max_errors:
                # reached maximun number of consecutive errors so exit
                break
        else:
            # success - can scrape the result
            num_errors = 0

# 链接爬虫
def link_crawler(seed_url, link_regex):
    """ Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url]
    # keep track which URL's have seen before
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            # check if link matches expected regex
            if re.match(link_regex, link):
                # form absolute link
                link = urljoin(seed_url, link)
                print(link)
                # check if have already seen this link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

def get_links(html):
    """Return a list of links from html"""
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    print(webpage_regex.findall(html))
    return webpage_regex.findall(html)

if __name__ == '__main__':
    #print(urllib.request.__file__)
    # http://httpstat.us/500 该网址会始终返回 500 错误码
    #download('http://httpstat.us/500')
    #crawl_sitemap('http://example.webscraping.com/sitemap.xml')
    #crawl_sitema_by_id()
    link_crawler('http://example.webscraping.com', '/(index|view)/')

    print(re.match('/places/default/view/Afghanistan-1','/(index|view)/'))





















