# -*- coding: UTF-8 -*-
try:
    1/0
except NameError:#有异常时执行
    print 'Name error'
else:#没有异常时执行
    print 'something else'
finally:#总会执行
    print 'always do'