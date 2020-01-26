# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:26:15 2020

@author: Pedro
"""
'''
s = "string"
s = input("Type your string: ")
current_answer = ""
answer = ""
current_letter = 0
count = 0

#iteration for every letter in the string 's'
for letter in s:
#reset variables for every iteration
    count = 0
    current_answer = ""
#checking the max length for every alphabetical string
    while (current_letter + count < (len(s)-1)):
#check if next letter is in alphabetical order
#if that is true, add it to current answer
#if not, break the loop
        print("Current letter is: " + s[current_letter])
        print("Current answer is: " + current_answer)
        if (ord(s[current_letter+count]) <= ord(s[current_letter+count+1])):
            print("letter " + s[current_letter+count] + " is smaller or equal than " + s[current_letter+count+1])
            current_answer += s[(current_letter+count)]
            count += 1
        else:
            print("letter " + letter + " is bigger than " + s[count])
            break
#compare size of current_answer and answer; if bigger, current_answer 
#becomes answer
    print("current answer is: " + current_answer + " ; length is: " + str(len(current_answer)))
    if (len(current_answer) > len(answer)):
        print("'" + current_answer + "` is bigger than " + answer + " ; swapping...")
        answer = current_answer
        
    current_letter += 1
    

print(answer)    
'''

'''
#this code worked
s = "string"
s = input("type your string :")
print("string length is: " + str(len(s)))

cur_answer = "" #currently evaluated answer
fin_answer = "" #final answer with biggest length
count = 0       #counter
cur_letter = 0  #counter to know with letter we are evaluating the alphabetical string length 

for letter in s:    #for every letter in the string s, we should calculate the lengthiest string in alphabetic order
    
    count = 0       #reset our counter and current answer for every iteration
    cur_answer = ""
    cur_answer += s[cur_letter] #every calculated string will begin with the letter being evaluated
    
    while(count+cur_letter < (len(s)-1)): #while the position of the current letter + our counter is smaller than the length of the string
        print("This iteration, count is: " + str(count))
        print("This iteration, cur_letter is: " + str(cur_letter))
        print("This iteration, comparing " + s[count+cur_letter] + " with " + s[count+cur_letter+1])
        if(count+cur_letter >= len(s)): #if the counter + the current letter counter is bigger or equal than the length of the original string
            print("reached the end for the letter " + s[cur_letter]) #so we break the loop
            break
        elif(ord(s[count+cur_letter]) <= ord(s[count+cur_letter+1])): #if the value of the current letter is less than or equal to the next letter in the sequence
            cur_answer += s[count+cur_letter+1] #we then add it to the current answer
            print(s[count+cur_letter] + " added to the current answer.")
            print("so far, the current answer is " + cur_answer)
            count += 1                        #and increase the counter by 1
            
        else:
            print("next letter isnt in alphabetical order.")
            break
    
    if(len(cur_answer) > len(fin_answer)):  #if the length of the currently evaluated alphabetical string is bigger than the current final string, then the
        print("New answer! Changed from " + fin_answer + " to " + cur_answer)
        fin_answer = cur_answer             #then the current evaluated string becomes our final answer
    else:
        print("the answer wasn`t changed this iteration. It`s still " + fin_answer)
    
    cur_letter += 1 #having finished the iteration for a single character, we jump to the next and increase this counter
    
print(fin_answer)
'''

cur_answer = "" #currently evaluated answer
fin_answer = "" #final answer with biggest length
count = 0       #counter
cur_letter = 0  #counter to know with letter we are evaluating the alphabetical string length 
for letter in s:    #for every letter in the string s, we should calculate the lengthiest string in alphabetic order
    
    count = 0       #reset our counter and current answer for every iteration
    cur_answer = ""
    cur_answer += s[cur_letter] #every calculated string will begin with the letter being evaluated
    
    while(count+cur_letter < (len(s)-1)): #while the position of the current letter + our counter is smaller than the length of the string
        if(count+cur_letter >= len(s)): #if the counter + the current letter counter is bigger or equal than the length of the original string
            break
        elif(ord(s[count+cur_letter]) <= ord(s[count+cur_letter+1])): #if the value of the current letter is less than or equal to the next letter in the sequence
            cur_answer += s[count+cur_letter+1] #we then add it to the current answer
            count += 1                        #and increase the counter by 1
        else:
            break
    if(len(cur_answer) > len(fin_answer)):  #if the length of the currently evaluated alphabetical string is bigger than the current final string, then the
        fin_answer = cur_answer             #then the current evaluated string becomes our final answer
    else:
    cur_letter += 1 #having finished the iteration for a single character, we jump to the next and increase this counter
    
print(fin_answer)