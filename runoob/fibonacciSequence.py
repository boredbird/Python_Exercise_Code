# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:44:20 2016

@author: zhangchunhui
"""

#
#def fib(n):
#    a,b=1,1
#    for i in range(n-1):
#        a,b=b,a+b
#    return a

#def fib(n):
#    if n==1 or n==2:
#         return 1
#    return fib(n-1)+fib(n-2)
#    

def fib(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs=[1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs