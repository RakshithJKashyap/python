# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:46:52 2021

@author: raksh
"""

import calc_functions
print("\n1.Add\n2.Substarct\n3.Multiplication\n4.Division")
choice = input("Enter Your Choice:")
if choice in ('1','2','3','4'):
    a=float(input("enter the first number:"))
    b=float(input("enter the second number:"))
    if choice == '1':
        print("addition is {} ".format(calc_functions.addfunction(a,b)))
    elif choice == '2':
        print("Difference is {} ".format(calc_functions.subtraction(a,b)))
    elif choice == '3':
        print("Multiplication is",calc_functions.multiply(a,b))
    elif choice == '4':
        print(f"Dividend is{calc_functions.divide(a,b)}")
else:
        print("{0}".format('Worng Choice'))
              
