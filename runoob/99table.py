# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:26:07 2016

@author: zhangchunhui
"""
import time

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
for i in range(1,10):
    for j in range(1,10):
        result=i*j
        time.sleep(1)
        print('%d * %d = % 3d'%(i,j,result))      
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
