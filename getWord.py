#!/usr/bin/python3
# coding: utf-8

import requests
#import xml.etree.ElementTree as et
from bs4 import BeautifulSoup
import sys
import textwrap


class GetInfo():
    def __init__(self,url):
        self.url=url

    def get_wiki_info(self):
        res = requests.get(self.url)
        if res.status_code == 200:
             soup = BeautifulSoup(res.text, "html.parser")
             mean = soup.find("td", attrs={"class": "content-explanation ej"})
             key = soup.find("span",attrs={"id":"h1Query"})
             return  key.string ,mean.string
        else:
            return ""


keyword = input()
if (not keyword) or len(keyword) == 0:
    print("error")
    sys.exit()
#baseUrl3 = 'http://wikipedia.simpleapi.net/api?keyword={}&output=xml'

baseUrl3 = 'https://ejje.weblio.jp/content/{}'
baseUrl3 = baseUrl3.format(keyword)
print(baseUrl3)
getInfo = GetInfo(baseUrl3)
key, ret = getInfo.get_wiki_info()
str = "検索キー: %s \n %s" %(key,textwrap.fill(ret,20))
print(str)