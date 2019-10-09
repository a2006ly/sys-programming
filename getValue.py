import requests
from bs4 import BeautifulSoup

base_url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=3092.T"

res = requests.get(base_url)
soup = BeautifulSoup(res.text)

details = soup.find_all("div",id="detail")
restu = {}
for i in details:
    des =i.findAll("dt",class_="title")
    for f in des:
        restu[f.contents[0]]=""
    
    dds = i.findAll("dd",class_="ymuiEditLink mar0")
    for f in dds:
        print(f.strong.string)
