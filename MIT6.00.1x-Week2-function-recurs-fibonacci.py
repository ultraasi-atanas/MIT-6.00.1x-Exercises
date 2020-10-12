# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 10:51:12 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Fibonacci sequence

def fib(a):
    
    if (a == 0) or (a == 1):
        return 1
    else:
        return (fib(a-1) + fib(a-2))
    
print(fib(4))