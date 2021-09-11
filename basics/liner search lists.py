# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 00:22:50 2021

@author: raksh
"""

import sys
a=list()
n=int(input("enter the length of the list:"))

for i in range(0,n):
    ele=int(input("enter the elements of the list:"))
    a.append(ele)
print(a)
key=int(input("enter the key element to be searched:"))

for i in range(len(a)):
    if key == a[i]:
        print("key is found at",i+1)
        sys.exit()
print("key in not found")