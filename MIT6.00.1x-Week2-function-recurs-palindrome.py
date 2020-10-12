# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 10:51:12 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Palindrome check - does a string read the same backwards as forwards
# Recursively

def palindrome(string):
    '''
    Parameters
    ----------
    input: string : a continuous letters string, no other charaters.

    Returns
    -------
    result : boolean whether or not the input string is a palindrome
    '''
    
    result = True
    
    # longform - if (len(string) == 0) or (len(string == 1)):
    # but we have a shorter form
    if len(string) in (0,1):
        return result
    # check the first and last characters
    elif (string[0] == string[-1]):
        # now check the middle bit
        # perform a boolean operation with and
        # returns true if both are true
        # we call palindrome without both characters
        # slicing can be done with extended indexing syntax
        # a[start:stop:step]
        return (result and palindrome(string[1:len(string)-2]))
        
print(palindrome("222"))