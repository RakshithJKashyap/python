# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:54:20 2021

@author: raksh
"""

str= input("Enter a String : ")
vowels = 0
consonants = 0

for i in str:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Number of Vowels are= ", vowels)
print("Number of Consonants are= ", consonants)