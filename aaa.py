#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import requests
import urllib.parse
import xml.etree.ElementTree as et


#驛ｽ驕灘ｺ懃恁
def getPrefList():
    headers = {'X-API-KEY': 'EI2doWypPuoGk0G9eV8DNmuqqjPn4kaWvqCJNnaN'}
    URL1 = 'https://opendata.resas-portal.go.jp/api/v1/prefectures'
    freflist = requests.get(URL1,headers=headers).json()
    if freflist['message'] == None:
        return freflist['result']

#蟶ょ玄逕ｺ譚�
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


#荳�莠ｺ蠖薙◆繧雁慍譁ｹ遞�2008-2016蟷ｴ
def getcitytaxes(prefCode,cityCode):
    headers = {'X-API-KEY': 'EI2doWypPuoGk0G9eV8DNmuqqjPn4kaWvqCJNnaN'}
    URL1 = 'https://opendata.resas-portal.go.jp/api/v1/municipality/taxes/perYear?cityCode={}&prefCode={}'.format(cityCode,prefCode)
    citytaxes = requests.get(URL1,headers=headers).json()
    if citytaxes['message'] == None:
        return citytaxes['result']['data']

#荳�莠ｺ蠖薙◆繧願ｳ����5:30���34豁ｳ
def getcitymunicipality(prefCode):
    headers = {'X-API-KEY': 'EI2doWypPuoGk0G9eV8DNmuqqjPn4kaWvqCJNnaN'}
    URL1 = 'https://opendata.resas-portal.go.jp/api/v1/municipality/wages/perYear?prefCode={}&simcCode=-&wagesAge=5&sicCode=-'.format(prefCode)
    citytaxes = requests.get(URL1,headers=headers).json()
    if citytaxes['message'] == None:
        return citytaxes['result']['data']
            


if __name__ == "__main__":
    prefCode = ""
    cityCode = ""
    cityName = ""
    cityName = ""
    #querystr = input()
    querystr = '譚ｱ莠ｬ驛ｽ'
    if querystr != "":
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
            cityName = pref['cityName']
            #print(cityName)
            wikiinfo = getwiki(cityName)
            print("笆�{}縺ｮ邏ｹ莉�".format(cityName))
            print("    {}".format(wikiinfo))
            print()

            print("笆�{}縺ｮ{} 荳�莠ｺ蠖薙◆繧雁慍譁ｹ遞�2008-2016蟷ｴ��域ｯ主ｹｴ���".format(querystr,cityName))
            citytaxes = getcitytaxes(prefCode,cityCode)
            for taxe in citytaxes:
                print("    {}蟷ｴ��� {} 蜊����".format(taxe['year'],taxe['value']))
            print()

            print("笆�{}縺ｮ{} 荳�莠ｺ蠖薙◆繧願ｳ����5:30���34豁ｳ��域ｯ主ｹｴ���".format(querystr,cityName))
            citymunicipality = getcitymunicipality(prefCode)
            for municipality in citymunicipality:
                print("    {}蟷ｴ��� {} 荳����".format(municipality['year'],municipality['value']))
