# -*- coding: utf-8 -*-
"""
Created on Tue Oct 6 20:02:48 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""
# Function basics

x = 12
def g(x):
   x = x + 1
   def h(y):
      return x + y
   return h(6)
g(x)