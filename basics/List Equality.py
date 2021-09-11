# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:01:10 2021

@author: raksh
"""

listA=[1,2,3,4,5]
listB=[5,4,2,1,3,8]

count=0
for num in listA:
    for n in listB:
        if(num==n):
            count+=1

if(count==(len(listA) and len(listB))):
    print("List is equal") 


else:
     print('list is not equal')