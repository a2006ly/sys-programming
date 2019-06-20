# -*- conding:utf-8 -*-

#文字列処理
s="Hello"
s='Howdy'
print(s)

s="Hello"
s='h' + s[1:]
print(s)

s="Hello"
s[0]='h' #文字列の場合、indexで変更できません!!!!
print(s[0])

s="Hello"
s=s.lower()
print(s)

print('e' in s)
print('e' == s)
print(s.find("xy"))

#リスト処理
l = ['a','b','c']
print(l)

l = ['C','D','E']
print(l)

l = ['a','b','c']
l = ['GGG'] + l[1:]
print(l)

l = ['a','b','c']
l[0] = '0000'
print(l)

l = ['a','b','c']
l.append("yyyyy")
print(l)

l = ['a','b','c']
l.insert(0,"ssssss")
print(l)

#最後の項目
l = ['a','b','c']
l.pop()
print(l)


#何が違い？
del l[2]
l.pop(1)
print(c)

l = ['a','b','c']
if "a" in l:
    print("OK")



#FOR 0から右端含まない
for i in range(10):
    print(i)

for i in (0,7):
    tem = int(input())
    print(tem)

#リスト処理
l = [5,9,6,7,8]
l.append(["a","b"])
l.extend(["c","d"])
print(l)


#リスト処理 ソート
l = [5,9,6,7,8]
l.sort()
print(l)


l = [[5,9,6,7,8],[1,2,3],[121,12,13]]
def getSotKey(l):
    print(l[2])
    return  l[2]

l.sort(key=getSotKey)
print(l)





#fix_first
def fix_first(s):
    f = ""
    for i in range(len(s)):
        if i != 0 and s[0] == s[i] :
            f = f+"*"
        else:
            f = f+s[i]
    return f

print(fix_first("not aaa bnandn"))


#not_bad.py
def not_bad(s):
    str = ""
    i = 0
    notIndex = s.find("not")
    badIndex = s.find("bad")
    if notIndex < badIndex:
        str = s[notIndex + 3:].replace("bad","good")
        return  s[0 : notIndex + 3] + str
    else:
        return s

print(not_bad("bad not is "))
print(not_bad(" not is bad"))

#match_end.py
def match_end(s):
    strCount=0
    for str in s:
        #2文字以上   
        if len(str) >= 2:
            if str[0] == str[-1]:
                strCount += 1
    return strCount

print(match_end(["","aba","xx","bngghh","sdfds"]))

print(match_end(["","aba","","",""]))


#front_x.py
def front_x(x):	
    l  = list(x)
    l.sort(key=lambda s:s.startswith("x"),reverse=True)
    return l

#front_x.py
def front_x(x):	
    l  = list(x)
    return  sorted()

print(front_x(['bbb',	'ccc',	'axx',	'xzz',	'xaa']))	
print(front_x(['ccc',	'bbb',	'aaa',	'xcc',	'xaa']))	
print(front_x(['mix',	'xyz',	'apple',	'xanadu',	'aardvark']))

l =[1,2,2,2,2]
print(l)


#remove_adjacent.py
def remove_adjacent(li):	
    reList=[]
    for str in list(li):
        if li.count(str) > 1:
            li.remove(str)
    return li

print(remove_adjacent([1,	2,	2,	3]))	
print(remove_adjacent([2,	2,	3,	3,	3]))	
print(remove_adjacent([]))	

#linear_merge.py
def linear_merge(li1,	li2):	
    l = li1 + li2
    l.sort()
    return l

print(linear_merge(['aa',	'xx',	'zz'],	['bb',	'cc']))	
print(linear_merge(['aa',	'xx'],	['bb',	'cc',	'zz']))	
print(linear_merge(['aa',	'aa'],	['aa',	'bb',	'bb']))

#辞書
ip_adrs	=	{'aiit.ac.jp':	'175.184.120.230',	'g.aiit.ac.jp':	'210.190.118.224'}
for i in ip_adrs.keys():
    print(i)

 #辞書
ip_adrs	=	{'aiit.ac.jp':	'175.184.120.230',	'g.aiit.ac.jp':	'210.190.118.224'}
for i in ip_adrs.values():
    print(i)

#辞書
ip_adrs	=	{'aiit.ac.jp':	'175.184.120.230',	'g.aiit.ac.jp':	'210.190.118.224'}
for i in ip_adrs.items():
    print(i)
