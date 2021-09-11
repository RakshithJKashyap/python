# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:51:05 2021

@author: raksh
"""

x=int(input("enter the value of x coordinate:"))
y=int(input("enter the value of y coordinate:"))

if(x>=0 and y>=0):
    print(x,",",y,"are in 1st quadrant")
elif(x<=0 and y>=0):
    print(x,",",y,"are in 2nd quadrant")
elif(x<=0 and y<=0):
    print(x,",",y,"are in 3rd quadrant")
else:
    print(x,",",y,"are in 4th quadrant")