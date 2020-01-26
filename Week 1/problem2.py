# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:04:41 2020

@author: Pedro
"""

s = "azcbobobegghakl"
print(len(s))
count = 0
num = 0
for letter in s:
    if s[num:(3+num)] == 'bob':
        count += 1
    num += 1
print (count)
    
