# -*- coding: utf-8 -*-
"""
Created on Thu Oct 8 16:56:41 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Exercise: iter power - Your code must be iterative - use of the ** operator is not allowed. 
# Write an iterative function iterPower(base, exp) that calculates the exponential baseexp by simply using successive multiplication. For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. Write such a function below.
# This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed. 

# =============================================================================
# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#  
#     returns: int or float, base^exp
#     '''
#     result = 1
#     
#     if exp == 0:
#         return 1
#     elif exp == 1:
#         return base
#     elif base == 1:
#         return 1
#     else:    
#         while (exp > 0):
#             result = result * base
#             exp -= 1
#     return result
#             
# print(iterPower(2,40))
#     
# =============================================================================

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
            return 1
    elif exp == 1:
            return base
    elif base == 1:
            return 1
    else:    
            return base * recurPower(base,exp-1)

print(recurPower(0,2))