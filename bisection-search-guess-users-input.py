# -*- coding: utf-8 -*-
"""
Created on 15 SEPTEMBER 2020 

@author - Atanas Kozarev
"""
import math

hi = 99
low = 0
guess = math.ceil((hi+low)/2)

print("Please think of a number between 0 and 100!")
print("Is your secret number: " + str(guess), sep=" ", end="\n")
user_said = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

if user_said == 'l':
    low = guess
elif user_said == 'h':
    high = guess
elif user_said == 'c':
    print("Game over. Your secret number was: " + str(guess))
else 
    print("Sorry, I did not understand your input."")