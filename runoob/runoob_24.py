#!/usr/bin/python
# -*- coding: UTF-8 -*-

x=2.0
y=1.0
sum=0
for n in range(20):
	sum+=x/y
	x,y=x+y,x
print(sum)