#�֐���`�A���������l���w��
def add(x,y=2):
    return x+y
add(1,2)


#���� *:�c��̈��� �Ɓ@**�Fkey-valu�w�肳�ꂽ����
def func(x,y,*name,**kv):
    print(x)
    print(y)
    print(name)
    print(kv)

func(1,2,3,4,a='2')

#�����l��Ԃ�
def func():
    return 1,2
a,b = func()
print(a,b)

#globals�ϐ��A�ҏW�̏ꍇ�Aglobals
a=2
def func():
    global a
    print(a)
    a = a+ 1
    print(a)
func()

#�ł���[���֐����s�O��A���������s�������ꍇ
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
