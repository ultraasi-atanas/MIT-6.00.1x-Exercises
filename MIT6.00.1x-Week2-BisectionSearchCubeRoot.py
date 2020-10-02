#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:43:09 2020

@author: Atnaas Kozarev
"""

# Guess the Cube Root of Cube using Bisection search

cube = 27 
margin_of_error = 0.01
numGuesses = 0
low = 1.0
high = cube
guess = (high + low)/2.0

while abs(guess**3 - cube) >= margin_of_error:
    print('low = ' + str(low) + ' high = ' + str(high) + ' guess = ' + str(guess))
    numGuesses += 1
    if guess**3 < cube:
        low = guess 
    else:
        high = guess
    guess = (high + low)/ 2.0
print('numGuesses = ' + str(numGuesses))
print(str(guess) + ' is close to cube root of ' + str(cube))