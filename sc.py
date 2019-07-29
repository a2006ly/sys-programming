import requests
from bs4 import BeautifulSoup

#URLで年と月ごとの設定ができるので%sで指定した英数字を埋め込めるようにします。
base_url = "http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=%s&month=%s&day=1&view=a2"
#base_url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=3092.T"

#for文で2000年~2003年までの3回を回します。
for year in range(2000,2004):

#入れ子のforで1月~12月の12回を回します。
        for month in range(1,13):

                #for文で2000年1月...2月...3月と回せるので埋め込んで行きます。
                r = requests.get(base_url % (year,month))
                r.encoding = r.apparent_encoding

                #対象である表をスクレイピングしていきます。
                soup = BeautifulSoup(r.text)
                rows = soup.findAll('tr',class_='mtx')
                i = 1

                #表の最初の１〜３行目はカラム情報なのでスライスしていまいます。
                rows = rows[4:]

                #for文で1日〜最終日までの１行を取得します。
                for row in rows:
                        data = row.findAll('td')

#１行の中には様々なデータがあるので全部取り出してあげます。
                        for d in data:
                                print(d.text)
                        print("")