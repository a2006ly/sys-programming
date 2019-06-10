#!/usr/bin/python3
# -*- coding: utf-8 -*-

#メソッド定義、必須引数指定
def first_last(s):
    if len(s) > 1:
        s2 = s[0:2] + s[-2:]
        return s2
    else:
        return ""

#メソッド呼び出
print(first_last("spring")) 
print(first_last("hello"))  
print(first_last("a"))  
print(first_last("abc"))


#s1  =   "spring"    
#s2 = s1[:2] + s1[-2:]
#s2=s1[0]+s1[1]+s1[-2]+s1[-1]
#print(s2)

#s1  =   "hello" 
#s2 = s1[:2] + s1[-2:]
#s2 = s1[0:2] + s1[-2:]
#print(s2)

#s1  =   "abc"   
#s2 = s1[0:2] + s1[-2:-1]
#s2 = s1[0]+s1[1]+s1[4]+s1[5] #index error
#print(s2)
