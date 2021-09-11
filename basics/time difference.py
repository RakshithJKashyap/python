# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:13:14 2021

@author: raksh
"""





import datetime
time1= datetime.datetime.strptime(input('enter time in HH:MM format: '), "%H:%M")
print(time1.strftime("%H:%M"))
time2= datetime.datetime.strptime(input('enter time in HH:MM format: '), "%H:%M")
print(time2.strftime("%H:%M"))



time_diff=time1-time2
print(time_diff.total_seconds()/60)