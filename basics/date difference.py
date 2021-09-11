# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 00:21:37 2021

@author: raksh
"""

import datetime
date1= datetime.datetime.strptime(input('enter date '), "%d/%m/%Y")
print(date1.strftime("%d/%m/%Y"))
date2= datetime.datetime.strptime(input('enter date  '), "%d/%m/%Y")
print(date2.strftime("%d/%m/%Y"))
next_day = date1
while True:
    if next_day > date2:
        break
    print(next_day)
    next_day += datetime.timedelta(days=1)