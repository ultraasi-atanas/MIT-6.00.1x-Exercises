# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 06:35:04 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Bisection search - secret number game - guess users secret number 

high = 100
low = 0
#guess = int((high+low)/2) version with int()
guess = (high+low)//2
user_input =''
print("Please think of a number between 0 and 100!")

#GAME STARTS
while (user_input != 'c'):
    print("Is your secret number " + str(guess) + "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if user_input == 'l':
        #debugging with print("inputed letter is L - guess is lower than secret number")
        low = guess
        #re-doing the bisection calculation
        #guess = int((high+low)/2)
        guess = (high+low)//2
    elif user_input == 'h':
        #debugging with print("inputed letter is H - guess is higher than secret number")
        high = guess
        #re-doing the bisection calculation
        #guess = int((high+low)/2)
        guess = (high+low)//2
    elif user_input == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else: 
        print("Sorry, I did not understand your input.")
