# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 08:14:46 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Greatest common divisor
# Write an iterative function, gcdIter(a, b) 
# One easy way to do this is to begin with a test value equal to the smaller
# of the two input arguments, and iteratively reduce this test value by 1 
# until you either reach a case where the test divides both a and b without 
# remainder, or you reach 1. 

def smallest_f(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the smaller number of a & b.
    '''
    # which is the smaller number
    if ((a > b) or (a == b)):
        small = b
    else:
        small = a
    
    # print("smallest is " + str(small))
    return small
   

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # which is the smaller number
    test_num = smallest_f(a,b)
    # now we need to test does it divide a and b without a reminder
    # otherwise reduce test by 1, until test = 1
    
    if test_num == 1:
        return 1
    # next test potentially not needed - as 0 is not a positive integer
    elif test_num == 0:
        return 0
    
    while test_num > 0:
        if ((a % test_num) == 0 and (b % test_num) == 0):
            return test_num
        else:
            test_num = test_num - 1
    
    # print("I finished")

# print(gcdIter_f(4,50))