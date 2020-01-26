# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 12:23:39 2020

@author: Pedro
"""

varA = "2"
varB = 2

if (type(varA)==str or type(varB)==str):
    print("string involved")
elif (varA > varB):
    print("bigger")
elif (varA == varB):
    print("equal")
else:
    print("smaller")
    
