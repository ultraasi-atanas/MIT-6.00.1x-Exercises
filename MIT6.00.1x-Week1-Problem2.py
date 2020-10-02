#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:24:04 2020

@author: Atanas Kozarev

Exam Week 1
Problem 2 
0.0/10.0 points (graded)
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2

"""

# given s

s = 'azcbobobegghakl'

# =============================================================================
# get a character
# is it b - No - Next character
#         - Yes - Check next characters is the next two an on and a b bob that follows?
#  how do I advance to the next character if I use letter in s - i can't
#  what other examples of traversing a string did I have
# =============================================================================

index = 0
bob_found = 0


for index in range(0,len(s)):
    if (s[index] == 'b') and (s[index+1]) == 'o' and (s[index+2] == 'b'):
                bob_found += 1
print("Number of times bob occurs is: " + str(bob_found))

# =============================================================================
# for index in range(0,len(s)):
#     # print(s[index])
#     if (s[index] == 'b'):
#         if (s[index+1]) == 'o':
#             if (s[index+2] == 'b'):
#                 bob_found += 1
#             
# print("Number of times bob occurs is: " + str(bob_found))
#     # I want to know how this compares computationally     
# 
# =============================================================================

