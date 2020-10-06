# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 09:24:27 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Binary - turning float numbers into binary

user_input = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*user_input) %1 != 0:
    print('Reminder = ' + str((2**p)*user_input - int((2**p)*user_input)))
    p += 1
    
num = int(user_input*(2**p))

result = ''
if num == 0:
    result = '0'

while num > 0:
    result = str(num%2) + result
    num = num // 2
    
for i in range (p - len(result)):
    result = '0' + result    
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(user_input) + ' is ' + str(result))