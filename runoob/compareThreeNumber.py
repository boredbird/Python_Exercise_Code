# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:35:04 2016

@author: zhangchunhui
"""
##runfile('D:/plug/python_exercise_code/compareThreeNumber.py', wdir='D:/plug/python_exercise_code')
##输入三个整数x,y,z，请把这三个数由小到大输出。
l=[]
for i in range(3):
    x=int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)
