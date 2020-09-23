#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:13:47 2020

@author: Atanas Kozarev

Exam Week 1
Problem 1 
0.0/10.0 points (graded)
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5


"""
# given s

s = 'azcbobobegghakl'

vowels = 0

for aLetter in s:
    if (aLetter == 'a') or (aLetter == 'e') or (aLetter == 'i')  or (aLetter == 'o') \
    or  (aLetter == 'u'):
        vowels += 1
        
print("Number of vowels: " + str(vowels))