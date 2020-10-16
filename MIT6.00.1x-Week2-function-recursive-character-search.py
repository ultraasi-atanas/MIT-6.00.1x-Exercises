# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 10:51:12 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""

# =============================================================================
# We can use the idea of bisection search to determine if a character is in a string, 
# so long as the string is sorted in alphabetical order.
# 
# First, test the middle character of a string against the character you're looking for 
# (the "test character"). If they are the same, we are done - we've found the character 
#  we're looking for!
# 
# If they're not the same, check if the test character is "smaller" than the middle character.
# If so, we need only consider the lower half of the string; otherwise, we only consider the 
#  upper half of the string. (Note that you can compare characters using Python's < function.)
# 
# Implement the function isIn(char, aStr) which implements the above idea recursively to test 
# if char is in aStr. char will be a single character and aStr will be a string that is in
# alphabetical order. The function should return a boolean value. 
# 
# =============================================================================

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # print("Function call")
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return (char == aStr[0])
    
    # Finding the half
    halfPos = int(len(aStr)/2)
    middleChar = aStr[halfPos]
    
    # Comparing the middle character with the test character
    if char == middleChar:
        return True
    elif char < middleChar:
        return isIn(char,aStr[:halfPos])
    else:
        return isIn(char,aStr[halfPos+1:])
    
print(isIn("b","abcdefghi"))