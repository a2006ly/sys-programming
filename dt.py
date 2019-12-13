#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime

str_day = '2016/01/15 09:15:31'
one_day = datetime.datetime.strptime(str_day, '%Y/%m/%d %H:%M:%S')
print(one_day)  # -> 2016-01-15 09:15:31
print(type(one_day))

str_date = '2016”N12ŒŽ31“ú'
one_day = datetime.datetime.strptime(str_date, '%Y”N%mŒŽ%d“ú')
print(one_day)  # -> 2016-12-31 00:00:00

print(datetime.datetime.now())
dt = datetime.datetime.now()
print(type(dt))
dtToString = datetime.datetime.strftime(dt,'%Y/%m/%d %H:%M:%S')
print(type(dtToString))


print(datetime.datetime.now().year)
print(datetime.datetime.now().month)


dt1 = '2019/01/02'
dt2 = '2019/02/02'
d1 = datetime.datetime.strptime(dt1,'%Y/%m/%d')
d2 = datetime.datetime.strptime(dt2,'%Y/%m/%d')

d3 = d1 - d2
print(d3)

td_10d = datetime.timedelta(days=10)
print(d1  + td_10d)

