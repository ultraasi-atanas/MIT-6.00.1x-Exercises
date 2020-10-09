# -*- coding: utf-8 -*-
"""
Created on Tue Oct 6 20:02:48 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Function basics

def func_a():
    print("I am inside func_a")

def func_b(y):
    print("I am inside func_b")
    return y

def func_c(z):
    print("I am inside func_c")
    return z()

print(func_a())
print(5 + func_b(3))
print(func_c(func_a))