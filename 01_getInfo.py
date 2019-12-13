import requests
import urllib.parse
import sys
import xml.etree.ElementTree as et
import textwrap
import json


class getinfo():
    def __init__(self,url,headers):
        self.headers=headers
        self.url = url
        
    def openUrt(self):
        res:requests.Response
        res = requests.get(self.url,headers = self.headers)
        return res.text

   

HEADERS = {'X-API-KEY': 'EI2doWypPuoGk0G9eV8DNmuqqjPn4kaWvqCJNnaN'}
URL1 = 'https://opendata.resas-portal.go.jp/api/v1/prefectures'

ginfo = getinfo(URL1,HEADERS)
res = ginfo.openUrt()
rdata = json.loads(str(res))
for i in rdata['result']:
    print("prefCode{} prefName{}".format(i['prefCode'],i['prefName']))

#一人当たりのチキン
baseUrl = 'https://opendata.resas-portal.go.jp/api/v1/municipality/wages/perYear?'
prefCode=1
param = 'prefCode={}&simcCode=-&wagesAge=5&sicCode=-'.format(prefCode)
URL5 = baseUrl + param

ginfo = getinfo(URL5,HEADERS)
res = ginfo.openUrt()
retJson = json.loads(res)
print(retJson['result'])
print(retJson['result']['data'])

for i in retJson['result']['data']:
    print("年%s ち%s" %(i['year'],i['value']))
