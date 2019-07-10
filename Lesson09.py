# -*- coding: utf-8 -*-
import csv


path = '''C:\Users\user\Desktop\workspace\doc\sysp\test.csv'''
f = open(path,"w")

w = csv.writer(f)
w.writerow(['a','b','c'])
w.writerow(['1','2','3'])
f.close()


f = open(path + "test.csv","rU")
r = csv.reader(f)
for row in r:
	print(row)

f.close()


