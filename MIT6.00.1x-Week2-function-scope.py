# -*- coding: utf-8 -*-
"""
Created on Mon Oct 5 07:29:26 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Function basics

def is_even(i):
    """
    Parameters
    ----------
    i : decimal integer
        THIS FUNCTION RETURNS TRUE IF PARAMETER i IS EVEN NUMBER.

    Returns
    -------
    True or False

    """
    
    print("Hi")
    return i % 2 == 0

print(is_even(2)