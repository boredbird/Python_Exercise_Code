#!/usr/bin/python
# -*- coding: UTF-8 -*-

sum=0
for n in range(1,21):
	tmp=1
	for i in range(1,n+1):
		tmp*=i
	sum+=tmp
print(sum)