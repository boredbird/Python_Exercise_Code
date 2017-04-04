#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = ['one', 'two', 'three']
for i in a[::-1]:
	print(i)

L = [1,2,3,4,5]
s1 = ';'.join(str(n) for n in L)
print(s1)


def hello_world():
    print('hello world')

def three_hellos():
    for i in range(3):
        hello_world()

if __name__ == '__main__':
    three_hellos()