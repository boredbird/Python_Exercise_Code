#!/usr/bin/python
# -*- coding: UTF-8 -*-
m=['a','b','c']
n=['x','y','z']

for i in range(3):
	var=[n[i]]
	for j in range(2):
			var.append(n[j])
			if len(set(n)&set(var))==3  and var[0] !='x' and var[2]=='y' :
				print(var)