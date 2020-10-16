# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:00:41 2020

@author: Atnaas Kozarev - github.com/ultraasi-atanas
Week 2 MIT 6.00.1x Introduction to Computer Science and Programming Using Python

https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2020a
"""

# =============================================================================
# Write a function called polysum that takes 2 arguments, n and s. 
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.
# 
# =============================================================================

def polysum(n,s):
    '''

    Parameters
    ----------
    n : positive integer - number of polygon sides
    s : positive float - length of polygon sides

    Returns
    -------
    result : sum of the area and square of the perimeter of 
            the regular polygon rounded to 4 decimal places

    '''
    
    import math
    
    # Square of the perimeter
    sq_perim = (n*s)**2
    
    # Area calculation
    area = (0.25 * n * (s**2)) / (math.tan(math.pi / n))
    
    # Rounding result to 4 decimal places as per task
    return round((sq_perim + area),4)

print(polysum(4,3.50))