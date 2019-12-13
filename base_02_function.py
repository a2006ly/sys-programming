#関数定義、引数初期値を指定
def add(x,y=2):
    return x+y
add(1,2)


#引数 *:残りの引数 と　**：key-valu指定された引数
def func(x,y,*name,**kv):
    print(x)
    print(y)
    print(name)
    print(kv)

func(1,2,3,4,a='2')

#複数値を返す
def func():
    return 1,2
a,b = func()
print(a,b)

#globals変数、編集の場合、globals
a=2
def func():
    global a
    print(a)
    a = a+ 1
    print(a)
func()

#でこれーた関数実行前後、処理を実行したい場合
def dc(func):
    def wrapper():
        print("start")
        func()
        print("end")

    return wrapper

@dc
def hello():
    print("1234")

hello()
