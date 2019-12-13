
#クラスはインスタンス変数とクラス変数を持つことが出来ます。
#インスタンス変数はインスタンスう毎に独立
#クラス変数全インスタンス共有
class myclass():
    CLASS_VAR=0 #クラス変数
    
    def __init__(self):
        self.name="zhao"
        self.agge=16
        myclass.CLASS_VAR += 1

a = myclass()
b = myclass()
print(a.CLASS_VAR)


#参照制御_で始まる変数や関数外から参照しない「習慣」
#参照制御__で始まる変数や関数外から参照できない
#__init__インスタンス作成時実行
#__del__インスタンス削除時実行
#__str__インスタンス文字列化
#継承、多重継承の場合、クラスとコンマで区切り
class p:
    def __init__(self,na):
        self.name=na

class t(p):
    def aa (self):
        print(self.name)
tt = t("vvv")
tt.aa()


#super 第一引数は自分のクラス名、第2引数はインスタンス
class MyClass1(object):
    def __init__(self):
       self.val1 = 123

class MyClass2(MyClass1):
    def __init__(self):
        super(MyClass2, self).__init__()
        self.val2 = 456

a = MyClass2()
print(a.val1)                #=> 123
print(a.val2)                #=> 456