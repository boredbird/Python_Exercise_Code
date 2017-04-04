import numpy as np 
import theano.tensor as T 
from theano import function

#basic
x = T.dscalar('x')
y = T.dscalar('y')
z = x + y
f = function([x,y],z)

print(f(2,4))