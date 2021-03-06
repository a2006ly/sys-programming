#!/usr/bin/python3

'''
要件:
    数字3で割れる時はFizz
    数字5で割れる時はBuzz
    数字15で割れる時はFizzBuzz

実現構想:
    1.　ブール演算子の短絡評価特徴を利用して、　[and と or]を組み合わせで実現する（1行で実現）。
           x or y　  x が偽なら y, そうでなければ x
   　　    x and y   x が偽なら x, そうでなければ y
    
    2. 「辞書(key,value)　と　while」を利用して実現する（6行で実現）。
            除数と出力文字列をペア形で辞書に保存
            while の条件真と判定された場合、辞書から除数と対応の文字列取得
    
    3.  map関数、filter関数とlambdaを組み合わせで実現する（7行で実現）。
            map関数でループ処理を行う
            filter関数で条件チェックを行う
            lambdaは計算処理を行う

実現方法：
    Function Name :
        fb

    Parameters:
        n : int
        1から200までの数字

    Returns:
        数字3で割れる時はFizz
        数字5で割れる時はBuzz
        数字15で割れる時はFizzBuzz
'''



'''
実現方法1
    and 左が真のときにのみ、右が評価されます、右側の値を返す。
    or  左が偽のときにのみ、右が評価されます。
    上記以外の場合、空文字を返す
'''

def fb1(n):
    return n % 15 == 0 and "FizzBuzz" or n % 5 == 0 and "Buzz" or n % 3 == 0 and "Fizz" or 1 == 1 and ""

i = 1
while i <= 200:
    print(i,fb1(i))
    i = i + 1



'''
実現方法2
    whileの判定が真のときにのみ、キー対応の値を返す
    以外の場合、空文字を返す
'''

def fb2(n):
    dic = {15:"FizzBuzz",5:"Buzz",3:"Fizz"}
    for key in dic.keys():
        while (n % key == 0):
             return dic[key]
    return ""

i = 1
while i <= 200:
    print(i,fb2(i))
    i = i + 1



'''
実現方法3
    mapとfilterを使て、条件を合った値を返す
    以外の場合、空文字を返す
'''

def fb3(n):
    dic = {15:"FizzBuzz",5:"Buzz",3:"Fizz"}
    try:
       ll = list(filter(lambda x : n % x == 0, map(lambda k:k,dic.keys())))
       return dic[ll[0]]
    except :
       return ""

i = 1
while i <= 200:
    print(i,fb3(i))
    i = i + 1