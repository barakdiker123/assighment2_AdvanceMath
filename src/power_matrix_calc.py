#!/usr/bin/env python3


import numpy
from numpy.linalg import matrix_power
input_array = numpy.array([[0,1,1,1], [1,0,1,0],[1,1,0,1],[1,0,1,0]])
A_to_power6 = matrix_power(input_array, 6)
sum_var = 0
for row in A_to_power6:
    for elem in row:
        sum_var += elem
print(int(sum_var/2))
