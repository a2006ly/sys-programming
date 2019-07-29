#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import requests
import urllib.parse
import xml.etree.ElementTree as et

def getPrefList():
    headers = {'X-API-KEY': 'EI2doWypPuoGk0G9eV8DNmuqqjPn4kaWvqCJNnaN'}
    URL1 = 'https://opendata.resas-portal.go.jp/api/v1/prefectures'
    freflist = requests.get(URL1,headers=headers).json()
    if freflist['message'] == None:
        return freflist['result']

def getcityInfo(prefCode):
    headers = {'X-API-KEY': 'EI2doWypPuoGk0G9eV8DNmuqqjPn4kaWvqCJNnaN'}
    URL1 = 'https://opendata.resas-portal.go.jp/api/v1/cities?prefCode={}'.format(prefCode)
    cityInfo = requests.get(URL1,headers=headers).json()
    if cityInfo['message'] == None:
       return cityInfo['result']



#wikiAPI
def getwiki(cityName):
    URL1 = "http://wikipedia.simpleapi.net/api?keyword={}&output=xml".format(cityName)
    f = requests.get(URL1)
    root = et.fromstring(f.text)
    return root.findall('result/body')[0].text


def getcitytaxes(prefCode,cityCode):
    headers = {'X-API-KEY': 'EI2doWypPuoGk0G9eV8DNmuqqjPn4kaWvqCJNnaN'}
    URL1 = 'https://opendata.resas-portal.go.jp/api/v1/municipality/taxes/perYear?cityCode={}&prefCode={}'.format(cityCode,prefCode)
    citytaxes = requests.get(URL1,headers=headers).json()
    if citytaxes['message'] == None:
        return citytaxes['result']['data']

def getcitymunicipality(prefCode):
    headers = {'X-API-KEY': 'EI2doWypPuoGk0G9eV8DNmuqqjPn4kaWvqCJNnaN'}
    URL1 = 'https://opendata.resas-portal.go.jp/api/v1/municipality/wages/perYear?prefCode={}&simcCode=-&wagesAge=5&sicCode=-'.format(prefCode)
    citytaxes = requests.get(URL1,headers=headers).json()
    if citytaxes['message'] == None:
        return citytaxes['result']['data']
            


if __name__ == "__main__":
    prefCode = ""
    cityCode = ""
    querycityName = ""
    #querystr = input()

    if querystr == "":
            querystr = '東京都'

    freflist = getPrefList()
    for fref in freflist:
        if str(fref['prefName']) == querystr:
            prefCode = fref['prefCode']
            print(prefCode)


    if prefCode != "":
        cityInfo = getcityInfo(prefCode)
        for pref in cityInfo:
            #if pref['cityName'] == cityName.strip():
            cityCode = pref['cityCode']
            if querycityName != "":
                cityName = querycityName
            else:
                cityName = pref['cityName']

            if cityName.endswith("区"):
            #print(cityName)
                wikiinfo = getwiki(cityName)
                print("■{}の紹介".format(cityName))
                print("    {}".format(str(wikiinfo)))
                print()

                print("■{}の{} 一人当たり地方税2008-2016年（毎年）".format(querystr,cityName))
                citytaxes = getcitytaxes(prefCode,cityCode)
                for taxe in citytaxes:
                    print("    {}年： {} 千円".format(taxe['year'],taxe['value']))

                print()

                print("■{}の{} 一人当たり賃金5:30～34歳（毎年）".format(querystr,cityName))
                citymunicipality = getcitymunicipality(prefCode)
                for municipality in citymunicipality:
                    print("    {}年： {} 万円".format(municipality['year'],municipality['value']))
                print()
                
                if querycityName != "":
                    break