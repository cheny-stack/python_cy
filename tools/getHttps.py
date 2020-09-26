'''
使用Python爬取一个网页的全部域名
'''

#coding:utf-8
import requests
import re
from lxml import etree
from urllib.parse import urlparse


domains = set() # 域名去重列表，默认为空

# 方法一：使用正则匹配
proxies = {
    "http": "http://127.0.0.1:1080",
    "https": "http://127.0.0.1:1080",
}
domain = 'http://www.radiotaiwan.tw/zhong-guang-yin-le-wang-i-radio-fm963'  # 请求网址的域名
html = requests.get(domain ,proxies=proxies).text
s = re.findall(r'http[^\/]{1,2}//([^(\/| |")]+)', html)
all_domain = set(s)
with open('D:/tools/SSR-win/pac.txt') as my_file:
 pac_all =my_file.read()
 for d in all_domain:
     if d not in pac_all:
        print(" \"||" + d+"\",")


# 方法二：使用判断
'''
tree = etree.HTML(html)
def match_link(links):
    for link in links:
        if not re.match(r'(//|http|https).*', link):
            continue
        if str(link).startswith('//'):
            link = domain+link
        res = urlparse(link)
        domains.add(res.netloc)
href_links = tree.xpath('//@href')
match_link(href_links)
src_link = tree.xpath('//@src')
match_link(src_link)
print(domains)
'''
print('*'*100)

