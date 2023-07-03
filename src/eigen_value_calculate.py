#!/usr/bin/env python3

import numpy as np
from numpy.linalg import eig
input_array = np.array([[0,1,1,0],
                           [0,0,0,1],
                           [1,1,0,0],
                           [1,0,1,0]])
w,v=eig(input_array)
print(w)

import numpy
from numpy.linalg import matrix_power
input_array = numpy.array([[0,1,1,0],
                           [0,0,0,1],
                           [1,1,0,0],
                           [1,0,1,0]])
A_to_power6 = matrix_power(input_array, 8)
print(A_to_power6)
# output is 23
