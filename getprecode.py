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
            querystr = '�����s'

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

            if cityName.endswith("��"):
            #print(cityName)
                wikiinfo = getwiki(cityName)
                print("��{}�̏Љ�".format(cityName))
                print("    {}".format(str(wikiinfo)))
                print()

                print("��{}��{} ��l������n����2008-2016�N�i���N�j".format(querystr,cityName))
                citytaxes = getcitytaxes(prefCode,cityCode)
                for taxe in citytaxes:
                    print("    {}�N�F {} ��~".format(taxe['year'],taxe['value']))

                print()

                print("��{}��{} ��l���������5:30�`34�΁i���N�j".format(querystr,cityName))
                citymunicipality = getcitymunicipality(prefCode)
                for municipality in citymunicipality:
                    print("    {}�N�F {} ���~".format(municipality['year'],municipality['value']))
                print()
                
                if querycityName != "":
                    break