#!/usr/bin/python3
'''
要件:
    Unixのnlコマンドの基本機能相当のnl.pyを書く
    テキストデータは、ファイル名が指定されればファイルから、ファイル名が無ければstdinから読み込んでください。
    ファイル名が不正であればエラー処理

実現構想:
    1.readlines()メソッドでファイルを読み込んで、リストに格納して、リストをループしながら出力、
      サイズが大きすぎると、メモリにいっぱいなる可能性がある。
    2.readline()メソッドで一行ずつ読み書きます。
    3.エラー処理はtry-except
'''

import sys

if len(sys.argv) > 1:
    try:
        f = open(sys.argv[1],"rU")
    except IOError:
        print("Sorry, the file " + sys.argv[1] + " does not exist.",    file=sys.stderr)
        sys.exit(1)
else:
    f = sys.stdin

i = 0
while True:
    try:
        lineword = f.readline() #ctrl+cの時、KeyboardInterruptエラーが発生可能
    except: # KeyboardInterrupt 例外を捕まえれば OK です 
        sys.exit(1)
    else:
        if not lineword:
            f.close()
            break
        if lineword.strip() != "":
            i += 1
            print("{} {}".format(i,lineword))
        else:
            print(lineword)  
   