import sys

#int��Long�𓝍�����Ă��܂��A�S��Int���g��
print(sys.maxsize)

#Flot��Complex
num = 1.2e3
comNum = 123J

#r��t����ƁA�G�X�P�[�v����
str = r"123123\"test"
print(str)

#Unicode������̏ꍇ�Au��t���܂��B���������鎞
str = '�e�X�g'
print(len(str))
#�o�C�g��̏ꍇ�Ab��t���܂�
str = b"�e�X�g"
print(len(str))


#m������t�H�[�}�b�g(%)

str = "ABC"
#�E��
print("|%5s|" % str)
#����
print("|%-5s|" % str)

#�����t��print
print("%+d" % -123)

# �S�̌�5�@������2
print("%5.2f" % 123.225)

#O����
print("%+4d" % 12)

#%% �������g�̕\��
print("%%%d" % 20)


#�ϐ���`�A�萔�K���I�啶���ŏ���
#__doc__�h�L�������g�X�g�����O
"""DOC"""

#���X�g�E�^�v���E����,set
a = [1,2,3,'f']
for i,k in enumerate(a):
    print(i,k)
#[n:m:s]n����m�Q��,s��΂�
print(a[1:4:2])

#���X�g����
b=['a','b','c','d']
print(a+b)
print(zip(a,b))


#�^�v���A�v�f�ύX�ł��Ȃ�
a =(1,"test")
b=[1,2,3]
print(a[0])

#List�ɕϊ�
print(list(a))
print(tuple(b))

#�����^
dic = {'a':1,'b':2}



#key-value�Q��
for k,v in dic.items():
    print(k,v)

for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)


#SET�d���Ȃ����X�g
a=set([2,2,3,4,5,2])
print(a)

#���X�g�֐� map�Afilter,reduce
a=[1,2,3]
print(list(map(lambda x:x*2,a)))
print([i * 2 for i in a])

#filter �^�̏ꍇ�̂݁A�o��
a=[1,2,3]
c = filter(lambda x:x!=2,a)
print(list(c))
print([i for i in a if i%2!=0])

#reduce �ŏ���2�v�f�������ɁA�������s��
a=[1,2,3]
print(list(reduce(lambda x,y:x+y,a)))


#���X�g����I�ȏ�����
a=[1,2,3]
b=[4,5,6]
print([x * y for x in a for y in b])



#�������Z
a = False

c = "123" if a else "456"
print(c)


#���䕶
a = 1
if a == 1:
    print(1)
elif a==2:
    print(2)
else:
    print(3)

#while�ALoop��������������AEND���s
a=1
while a == 1:
    print("ccccccccc")
    a = a+1
else:
    print("END")

#for�̕\��
a=u"����������"
for i in a:
    print(i)

#break Loop��������
for i in range(10):
    if i == 5:
        break
    print(i)

#continue
for i in range(10):
    if i == 5:
        continue
    print(i)


#�ُ폈�� try except else finally raise
a= 1

try:
    f = 12/a
except:
    print("�ُ�")
else:
    print("Other") # �G���[���������Ȃ������ꍇ�A���s
finally:
    print("����") #��Ɏ��s

#��O�𔭐�������
try:
    raise SystemError('�����ُ�')
except:
    print("234")

#with�\���@�����I�������N���[�Y
with open("123.txt",'w') as f:
    f.write("23")

with open("123.txt",'r') as f:
    print(f.read())

#seert���A���Ғʂ�ɐݒ肳��Ă��邩���m�F����
a=1
assert a==2

#pass�� �������Ȃ���
def leanpas():
    pass
leanpas()

#Del�� �I�u�W�F�N�g�폜��
x =5
print(x)
del(x)
print(x)


#print��
a = "name %(name)s age %(age)d"
print(a % {'name':'123','age':22})

#with open("123.txt",'w') as f:
#    f.write("23")

f = open("123.txt","w")
print('HELLo',f)

with open("123.txt",'r') as f:
    c=f.read()
    print(c)

#exec�����������X�N���v�g�Ƃ��āA���s
exec('print(123)')