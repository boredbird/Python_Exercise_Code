#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(0,7):
	for j in range(0,7):
		if abs(j-3)<=3-abs(i-3) :
			print('*', end='')
		else :
			print(' ', end='')
	print('\r\n')


