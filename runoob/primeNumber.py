#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

def isPrime(n):
	for i in range(2,int((n+1)/2)):
		if n%i==0:
			print('False!')
			return
	print('True!')

isPrime(29)