#!/usr/bin/python
# -*- coding: UTF-8 -*-

a=[2, 8, 6, 1, 78, 45, 34, 2]
m=3
n=len(a)
print(a)

# for i in range(m):
# 	a[i],a[n-1-i]=a[n-1-i],a[i]

# print(a)


for i in range(m):
	a[i],a[n-m+i]=a[n-m+i],a[i]

print(a)

