#!/usr/bin/python
# -*- coding: UTF-8 -*-

def age(n):
	if n==1 :
		return 10
	else:
		return age(n-1)+2

print(age(5))
