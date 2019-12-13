import urllib.request
import urllib.parse
from xml.etree.ElementTree import ElementTree

# �ΏۏZ�����邢�̓����h�}�[�N                                                        
# ADRS = "�i��擌���1-10-40"
# ADRS = "�a�J��_�{�O2"                                                              
ADRS = "�Y�ƋZ�p��w�@��w"
print("{}�̋߂��̃��X�g�����A�y����łˁB".format(ADRS))

KEYID = "�P�Q�R�S�T" # �e���擾                                 
URL1 = "https://www.geocoding.jp/api/?q={}".format(urllib.parse.quote(ADRS))
URL2 = "https://api.gnavi.co.jp/RestSearchAPI/20150630/?keyid={}".format(KEYID)

# �Z������ܓx�o�x�̎擾�iGeocoding API�j                                             
f = urllib.request.urlopen(URL1)
et = ElementTree()
et.parse(f)
lat = et.find("./coordinate/lat").text
lng = et.find("./coordinate/lng").text

# �ܓx�o�x���烌�X�g�������擾�iGnavi API�j                                         
url2 = '{}&latitude={}&longitude={}'.format(URL2, lat, lng)
f = urllib.request.urlopen(url2)
et = ElementTree()
et.parse(f)
for e in et.findall('./rest/name'):
    print("-", e.text)