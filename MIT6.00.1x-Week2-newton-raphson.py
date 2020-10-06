# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 10:46:37 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Newton-Raphson - cuts down the time to do generative guesses; very efficient

delta = 0.01 #our margin of error
y = 99.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= delta:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))

print('Square root of ' + str(y) + ' is about ' + str(guess))
print('numGuesses = ' + str(numGuesses))
