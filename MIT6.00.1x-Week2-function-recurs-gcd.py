# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 09:50:54 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Greatest Common Divisor - Recursive
# A clever mathematical trick (due to Euclid) makes it easy to find greatest 
# common divisors. Suppose that a and b are two positive integers: If b = 0, 
# then the answer is a; Otherwise, gcd(a, b) is the same as gcd(b, a % b) 
# Write a function gcdRecur(a, b) that implements this idea recursively.
 # This function takes in two positive integers and returns one integer. 

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    elif a == b:
        return a
    elif (a == 1) or (b == 1):
        return 1
    
    return gcdRecur(b, a % b)

print(gcdRecur(90,100))