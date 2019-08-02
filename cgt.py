def fb(n):
    s = ('FizzBuzz', '', '', 'Fizz', '', 
         'Buzz', 'Fizz', '', '','Fizz', 
         'Buzz', '', 'Fizz', '', '')
    return s[n % 15]

i = 1
while i <= 20:
    print(i, fb(i))
    i = i + 1



x = 10
y = 3
z = x / y
print("{0:} divided by {1:} equals {2:.3f} or {3:}".format(x, y, z, int(z)))


def mark_3rd(s):
    if len(s) < 3: return s
    s2 = s.replace(s[2], "*")
    return s2[:2] + s[2] + s2[3:]

print(mark_3rd("logging"))
print(mark_3rd("apple"))
print(mark_3rd("orange"))
print(mark_3rd("gooooogle"))
print(mark_3rd("i"))



def calc7(numbers):
    sum = 0
    i = 0
    double = False
    n = len(numbers)
    if n == 0: return -1
    while i < n:
        sum += numbers[i]
        if double:
            sum += numbers[i]
            double = False
        if numbers[i] == 7: double = True
        i += 1
    return sum

print(calc7([1, 2]))
print(calc7([3, 7]))
print(calc7([7, 5, 6]))
print(calc7([7, 9, 7, 9, 7, 9]))
print(calc7([]))




def past_verb(s):
    irregular = {
        "go": "gone",
        "put": "put",
        "write": "written",
        "find": "found",
        "read": "read",
        }
    c = ["a", "i", "u", "e", "o"]

    if s in irregular:
        return irregular[s]
    if s[-1] == "c":
        return s + "ked"
    if s[-1] == "e":
        return s + "d"
    if s[-1] == "y":
        if not s[-2] in c:
            return s[:-1] + "ied"
        else:
            return s + "ed"
    if not s[-1] in c and s[-2] in c and not s[-3] in c:
        return s + s[-1] + "ed"
    return s + "ed"
  
print(past_verb("play"))
print(past_verb("like"))
print(past_verb("try"))
print(past_verb("stop"))
print(past_verb("heat"))
print(past_verb("picnic"))
print(past_verb("go"))
print(past_verb("put"))
print(past_verb("refer"))
print(past_verb("omit"))
print(past_verb("rain"))
print(past_verb("need"))
print(past_verb("look"))



import re

s= "AA,BB,CC,DD"
words = re.split(r'¥W+', s.lower())
print(words)


import re
# rを付けることを推奨。
# バックスラッシュをそのままで分かりやすいため。
content = r'hellow python, 123, hel end.' 
pattern = 'hel'

co = re.compile(pattern)
ret = co.match(content)

if ret:
    print(ret)
    print(ret.group())


content = r'hellow python, 123, hel end.' 
pattern = 'hel'

comp = re.compile(pattern)
ret = comp.search(content)
if ret:
    print(ret.group())

import re
str = "aa bb cc dd aa"
pattern = "aa"

comp = re.compile(pattern)
ret = comp.findall(str)
if ret:
    print(ret)


import re

str = "wat BBBB CCCC aaaa"
patter = "\s\W"
str2 = re.split("\W",str)
print(str2)

ret = re.findall(patter,str)
if ret:
    print(ret)

str = "wat BBBB CCCC aaaa"
patter = "\sB+"





from collections import Counter
str = "wat BBBB CCCC aaaa"
d = Counter(str)
print(d)




d2 = dict(d.most_common(20))

import pickle
f = open("words.dict", "wb")
pickle.dump(d2, f)
f.close()

import pickle
f = open("words.dict", "rb")
d2 = pickle.load(f)
f.close()
print(d2)


import csv
import re
import pickle
from collections import Counter
str = "wat BBBB CCCC aaaa"
rel = re.split("\W",str)
d = Counter(rel)

f = open("aaal.dic","wb")
pickle.dump(d,f)
f.close()


f = open("aaal.dic","rb")
d=pickle.load(f)
print(d)
f.close()


f = open('words.csv', 'w')
w = csv.writer(f)
for k, v in d.most_common(20):
    w.writerow([k, v])
f.close()

f = open("words.csv","r")
w = csv.reader(f)



from tkinter import *
root = Tk()

def click(str):
    return lambda: msg.set(str)

msg = StringVar()
msg.set("Howdy")
label = Label(root, textvariable = msg)
left = Button(root, text = 'Click me', command = click('Left!'))
right = Button(root, text = 'Click me', command = click('Right!'))

left.pack(side=LEFT, ipadx=5, ipady=5)
label.pack(side=LEFT, ipadx=5, ipady=5)
right.pack(side=LEFT, ipadx=5, ipady=5)
root.mainloop()


from tkinter import *
                                                                                                                                                                          

root = Tk()

msg = StringVar()
msg.set("123")
label = Label(root, textvariable = msg)
left = Button(root,text="1234")
label.pack(side=LEFT, ipadx=5, ipady=5)
left.pack(side=LEFT, ipadx=5, ipady=5)
root.mainloop()


from tkinter import *
import random
root = Tk()
cv = Canvas(root, width = 256, height = 256)
cv.pack()

import time
def rand(): # cheap random number [0, 256)
    return int(time.time() * 1000000 % 256)

for n in range(1000):
    #x = random.random() * 256
    #y = random.random() * 256
    x = rand()
    y = rand()
    cv.create_oval(x - 2, y - 2, x + 2, y + 2)
root.mainloop()



import commands	
s = commands.getoutput("date	+'DATE:	%Y-%m-%d'")	
print(s)
ret = commands.getstatusoutput("date	+'DATE:	%Y-%m-%d'")	
print(ret)	


import	popen2	
stdout,	stdin,	stderr	=	popen2.popen3('cat	/etc/passwd')	
for	s in	stdout:		
    print(s)

import os
print(os.listdir('.'))

import urllib.request
from xml.etree.ElementTree	import	ElementTree
f = urllib.request.urlopen("http://zip.cgis.biz/xml/zip.php?zn=1500001")	
et = ElementTree(f)	
for	e in et.getroot():
    print(e)