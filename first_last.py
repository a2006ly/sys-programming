#!/usr/bin/python3

s1  =   "spring"    
#s2 = s1[:2] + s1[-2:]
s2=s1[0]+s1[1]+s1[-2]+s1[-1]
print(s2)

s1  =   "hello" 
#s2 = s1[:2] + s1[-2:]
s2 = s1[0:2] + s1[-2:]
print(s2)

s1  =   "abc"   
#s2 = s1[0:2] + s1[-2:-1]
#s2 = s1[0]+s1[1]+s1[4]+s1[5] #index error
print(s2)
