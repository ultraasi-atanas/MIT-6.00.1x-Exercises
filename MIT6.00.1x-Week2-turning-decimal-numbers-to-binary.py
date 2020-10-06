# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 09:14:32 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Binary - turning decimal numbers into binary

num = int(input("Please enter an integer number: ")) 
    
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''

if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2)+result
    num = num // 2
if isNeg:
    result = '-' + result

print(result)