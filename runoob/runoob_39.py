#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = [1,4,6,9,13,16,19,28,40,100]
b=29
print(a)

flag=0
for i in range(len(a)-1):
	if (a[i]<=b and a[i+1]>=b) or (a[i]>=b and a[i+1]<=b):
		a.insert(i+1,b)
		flag=1
		break
if flag==0:
	if a[len(a)-1]>a[0]:
		if a[0]>=b:
			a.insert(0,b)
		else:
			a.insert(len(a),b)
	else:
		if a[0]<=b:
			a.insert(0,b)
		else:
			a.insert(len(a),b)

print(a)


import random

#生成 10 到 20 之间的随机数
print (random.uniform(10, 20)  )