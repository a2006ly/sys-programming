import sys

#intとLongを統合されています、全部Intを使う
print(sys.maxsize)

#FlotとComplex
num = 1.2e3
comNum = 123J

#rを付けると、エスケープ無視
str = r"123123\"test"
print(str)

#Unicode文字列の場合、uを付けます。文字数える時
str = 'テスト'
print(len(str))
#バイト列の場合、bを付けます
str = b"テスト"
print(len(str))


#m文字列フォーマット(%)

str = "ABC"
#右寄せ
print("|%5s|" % str)
#左寄せ
print("|%-5s|" % str)

#符号付きprint
print("%+d" % -123)

# 全体桁5　少数後2
print("%5.2f" % 123.225)

#O埋め
print("%+4d" % 12)

#%% 自分自身の表示
print("%%%d" % 20)


#変数定義、定数習慣的大文字で書く
#__doc__ドキュメントストリング
"""DOC"""

#リスト・タプル・辞書,set
a = [1,2,3,'f']
for i,k in enumerate(a):
    print(i,k)
#[n:m:s]nからm参照,s飛ばす
print(a[1:4:2])

#リスト結合
b=['a','b','c','d']
print(a+b)
print(zip(a,b))


#タプル、要素変更できない
a =(1,"test")
b=[1,2,3]
print(a[0])

#Listに変換
print(list(a))
print(tuple(b))

#辞書型
dic = {'a':1,'b':2}



#key-value参照
for k,v in dic.items():
    print(k,v)

for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)


#SET重複ないリスト
a=set([2,2,3,4,5,2])
print(a)

#リスト関数 map、filter,reduce
a=[1,2,3]
print(list(map(lambda x:x*2,a)))
print([i * 2 for i in a])

#filter 真の場合のみ、出力
a=[1,2,3]
c = filter(lambda x:x!=2,a)
print(list(c))
print([i for i in a if i%2!=0])

#reduce 最初の2要素を引数に、処理を行う
a=[1,2,3]
print(list(reduce(lambda x,y:x+y,a)))


#リスト内包的な書き方
a=[1,2,3]
b=[4,5,6]
print([x * y for x in a for y in b])



#条件演算
a = False

c = "123" if a else "456"
print(c)


#制御文
a = 1
if a == 1:
    print(1)
elif a==2:
    print(2)
else:
    print(3)

#while、Loop処理完了した後、END実行
a=1
while a == 1:
    print("ccccccccc")
    a = a+1
else:
    print("END")

#forの表示
a=u"あいうえお"
for i in a:
    print(i)

#break Loop処理完了
for i in range(10):
    if i == 5:
        break
    print(i)

#continue
for i in range(10):
    if i == 5:
        continue
    print(i)


#異常処理 try except else finally raise
a= 1

try:
    f = 12/a
except:
    print("異常")
else:
    print("Other") # エラーが発生しなかった場合、実行
finally:
    print("完了") #常に実行

#例外を発生させる
try:
    raise SystemError('処理異常')
except:
    print("234")

#with構文　処理終了自動クローズ
with open("123.txt",'w') as f:
    f.write("23")

with open("123.txt",'r') as f:
    print(f.read())

#seert分、期待通りに設定されているかを確認する
a=1
assert a==2

#pass分 何もしない文
def leanpas():
    pass
leanpas()

#Del分 オブジェクト削除文
x =5
print(x)
del(x)
print(x)


#print文
a = "name %(name)s age %(age)d"
print(a % {'name':'123','age':22})

#with open("123.txt",'w') as f:
#    f.write("23")

f = open("123.txt","w")
print('HELLo',f)

with open("123.txt",'r') as f:
    c=f.read()
    print(c)

#exec引数文字をスクリプトとして、実行
exec('print(123)')