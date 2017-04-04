# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:13:12 2016

@author: zhangchunhui
"""

###IS Prime Number?
from math import sqrt
from sys import stdout

def isPrime(n):
    for i in range(2,int(sqrt(n))):
        if n % i ==0:
            return 0
    return 1