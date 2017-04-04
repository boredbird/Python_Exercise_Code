# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:56:28 2016

@author: zhangchunhui
"""

#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#solution:
#f(n)=2*f(n-2)+[f(n-1)-f(n-2)]
def rabbitCnt(n):
    if n==1 or n==2 :
        return 2
    else:
        return rabbitCnt(n-2)+rabbitCnt(n-1)
        