#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
        都道府県の市区町情報を取得
        例①：東京都の渋谷区の情報取得の場合、下記のコマンドを実行
        getinfo.py 東京都 渋谷区
        例②：東京都のすべて市区町の情報取得の場合、下記のコマンドを実行
        getinfo.py 東京都

"""

import urllib.request
import requests
import urllib.parse
import sys
import xml.etree.ElementTree as et


class GetData():

    def __init__(self,headers):
       self.headers = headers

    def getPrefList(self,url,type="r"):
        freflist = requests.get(url,headers = self.headers)
        if freflist.status_code == 200:
            freflist = freflist.json()
            if freflist['result'] != None:
                if type == "r":
                    return freflist['result']
                elif type == "d":
                    return freflist['result']['data']
                else:
                    return freflist['result']['years'][0]
            else:
                return ""

    def getwiki(self,url):
        f = requests.get(url)
        if f.status_code == 200:
            root = et.fromstring(f.text)
            ret = root.findall('result/body')
            if len(ret) > 0:
                return ret[0].text
            else:
                 return "WiKI紹介情報が見つかりません。"
    def checkExists(self,v,list):
        ret = False
        for tempV in list:
            if str(v) == tempV['cityName']:
                ret = True
                break
        return ret


if __name__ == "__main__":

    print("都道府県の市区町情報を取得","---例：getinfo.py 東京都 渋谷区")
    print()
    
    querystr = ""
    querycityName = ""
    prefCode = ""
    cityName = ""
    if (len(sys.argv) > 2):
        querystr = sys.argv[1]
        querycityName = sys.argv[2]
    elif (len(sys.argv) > 1):
        querystr = sys.argv[1]
        querycityName = '-'
    else:
        #querystr = '東京都'
        #querycityName = '渋谷区'
        querystr = '北海道'
        querycityName = '-'

    HEADERS = {'X-API-KEY': 'EI2doWypPuoGk0G9eV8DNmuqqjPn4kaWvqCJNnaN'} #キー

    gcdata = GetData(HEADERS)
    URL1 = 'https://opendata.resas-portal.go.jp/api/v1/prefectures'
    baseUrl2 = 'https://opendata.resas-portal.go.jp/api/v1/cities?prefCode={}'
    baseUrl3 = 'http://wikipedia.simpleapi.net/api?keyword={}&output=xml'
    
    try:
        freflist = gcdata.getPrefList(URL1)
        for fref in freflist:
            if str(fref['prefName']) == str(querystr):
                prefCode = fref['prefCode']

        if prefCode == "":
            print("「 {} 」都道府県が見つかりません、再確認ください。".format(querystr))
        else:
            
            URL2 = baseUrl2.format(prefCode)
            cityInfo = gcdata.getPrefList(URL2)
            for pref in cityInfo:
                cityCode = pref['cityCode']
                if querycityName == "-":
                    cityName = pref['cityName']
                else:
                    ret = gcdata.checkExists(querycityName,cityInfo)
                    if ret:
                        cityName = querycityName
                    else:
                            print("「 {} 」都道府県の「{}」市区町村が見つかりません、再確認ください。".format(querystr,querycityName))
                            break

                URL3 = baseUrl3.format(cityName)
                wikiinfo = gcdata.getwiki(URL3)
                print("■{}の{}の紹介".format(querystr,cityName))
                print("    {}".format(str(wikiinfo)))
                print()


                baseUrl = 'https://opendata.resas-portal.go.jp/api/v1/municipality/taxes/perYear?'
                param = 'cityCode={}&prefCode={}'.format(cityCode,prefCode)
                URL4 = baseUrl + param
                print("■{}の{} 一人当たり地方税2008-2016年（毎年）".format(querystr,cityName))
                citytaxes = gcdata.getPrefList(URL4,"d")
                for taxe in citytaxes:
                    print("    {}年： {} 千円".format(taxe['year'],taxe['value']))
                print()

                baseUrl = 'https://opendata.resas-portal.go.jp/api/v1/municipality/wages/perYear?'
                param = 'prefCode={}&simcCode=-&wagesAge=5&sicCode=-'.format(prefCode)
                URL5 = baseUrl + param
                print("■{}の{} 一人当たり賃金5:30～34歳（毎年）".format(querystr,cityName))
                citymunicipality = gcdata.getPrefList(URL5,"d")
                for municipality in citymunicipality:
                    print("    {}年： {} 万円".format(municipality['year'],municipality['value']))
                print()
        
                baseUrl = 'https://opendata.resas-portal.go.jp/api/v1/townPlanning/estateTransaction/bar?'
                print("■{}以降の不動産の面積あたり平均価格".format("2012"))
                for year in ['2010','2012','2013','2014','2015','2016','2017']:
                   param = 'year={}&prefCode={}&cityCode={}&displayType=1'.format(year,prefCode,cityCode)
                   URL6 = baseUrl + param
                   yearValue = gcdata.getPrefList(URL6,"y")
                   if yearValue != "":
                       print("    {}年： {:>12,} 円".format(yearValue['year']
                                                         ,yearValue['value'])) if yearValue != '' else ''
                print()
                if querycityName != "-":
                    break
    except KeyboardInterrupt:
        print("Ctrl+Cで停止しました")