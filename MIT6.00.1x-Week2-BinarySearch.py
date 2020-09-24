#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:43:09 2020

@author: Atnaas Kozarev
"""

# Guess the Square Root of X using binary search

x = 10000 
margin_of_error = 0.01
numGuesses = 0
low = 1.0
high = x
guess = (high + low)/2.0

while abs(guess**2 - x) >= margin_of_error:
    print('low = ' + str(low) + ' high = ' + str(high) + ' guess = ' + str(guess))
    numGuesses += 1
    if guess**2 < x:
        low = guess 
    else:
        high = guess
    guess = (high + low)/ 2.0
print('numGuesses = ' + str(numGuesses))
print(str(guess) + ' is close to square root of ' + str(x))