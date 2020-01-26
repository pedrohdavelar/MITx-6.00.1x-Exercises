# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:45:12 2020

@author: Pedro
"""

#code with input and visual feedback
s = 'wogtnncapobsp'
s = input("What is the string? :")
vowels = 0
for letter in s:
    if (letter == 'a'):
        print("a: Another vowel")
        vowels += 1
    elif (letter == 'e'):
        print("e: Another vowel")
        vowels += 1
    elif (letter == 'i'):
        print("i: Another vowel")
        vowels += 1
    elif (letter == 'o'):
        print("o: Another vowel")
        vowels +=1
    elif (letter == 'u'):
        print("u: Another vowel")
        vowels +=1
    else:
        print(letter + " isn`t a vowel.")
        
print("Number of vowels: " + str(vowels))


'''
#code without input and feedback, to be used as solution
vowels = 0
for letter in s:
    if (letter == 'a'):
        vowels += 1
    elif (letter == 'e'):
        vowels += 1
    elif (letter == 'i'):
        vowels +=1
    elif (letter == 'o'):
        vowels +=1
    elif (letter == 'u'):
        vowels +=1
    else:
        vowels +=0
print("Number of vowels: " + str(vowels))
'''