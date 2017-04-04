#!/usr/bin/python
# -*- coding: UTF-8 -*-
n=34
a=[]

for i in range(n):
	a.append(i+1)
print(a)

m=-1
temp=0

while m<temp :
	m=temp
	flag=1
	for i in range(n):
		if a[i]>0:
			if flag<3:
				a[i]=a[i]
				flag=flag+1
			else:
				flag=1
				a[i]=0
				temp=temp+1	
	print('loop...')
	
print(a)