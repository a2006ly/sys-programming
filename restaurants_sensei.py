mport urllib.request
import urllib.parse
from xml.etree.ElementTree import ElementTree

# 対象住所あるいはランドマーク                                                        
# ADRS = "品川区東大井1-10-40"
# ADRS = "渋谷区神宮前2"                                                              
ADRS = "産業技術大学院大学"
print("{}の近くのレストラン、楽しんでね。".format(ADRS))

KEYID = "１２３４５" # 各自取得                                 
URL1 = "https://www.geocoding.jp/api/?q={}".format(urllib.parse.quote(ADRS))
URL2 = "https://api.gnavi.co.jp/RestSearchAPI/20150630/?keyid={}".format(KEYID)

# 住所から緯度経度の取得（Geocoding API）                                             
f = urllib.request.urlopen(URL1)
et = ElementTree()
et.parse(f)
lat = et.find("./coordinate/lat").text
lng = et.find("./coordinate/lng").text

# 緯度経度からレストラン情報取得（Gnavi API）                                         
url2 = '{}&latitude={}&longitude={}'.format(URL2, lat, lng)
f = urllib.request.urlopen(url2)
et = ElementTree()
et.parse(f)
for e in et.findall('./rest/name'):
    print("-", e.text)