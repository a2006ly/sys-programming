import re

str = "AAA,BB,1BB,DD"
pat = "\w"

p = re.compile(pat)
c = p.match(str)
if c:
    print(c.group())

c1 = p.search(str)
print(c1.group())

p = re.compile("(\d)([A-Z]{2})")
c1 = p.search(str)
print(c1.group())

print(re.split("\d",str))

#import os
#import sys
#print(os.environ)
#status = os.system('dir')
#print(status,file=sys.stdout)

#import subprocess
#p = subprocess.Popen("dir",shell=True, stdout=subprocess.PIPE, 
#        stderr=subprocess.PIPE,
#        universal_newlines=True)

#a,b = p.communicate()
#if p.returncode == 0:
#    print(a)
#else:
##    print(b)

#import subprocess
#p = subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE
#                     ,universal_newlines=True)
#a,b=p.communicate()
#if p.returncode == 0:
#    print(a)
#else:
#    print(b)


import os
#print(os.listdir())
print(os.path.exists("aa"))
print(os.stat("."))

#import glob
#print(glob.glob("*.py"))
import datetime

t = datetime.datetime(2001,1,1)
print(t)
t = datetime.datetime.today()
print(t)


ct = datetime.datetime.today()
p = ct + 2
print(p)
p = ct + datetime.timedelta(days=2)

print(p)


ct = datetime.datetime
print(ct.strftime("%Y-%M-%d"))