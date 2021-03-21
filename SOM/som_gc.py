import tensorflow as tf
from math import *
import sys
from som import *
from tool_norm import *
import numpy as np
import os
#path="/home/yuan/Documents/TEST_SOM/"
   
inputs0 = np.loadtxt("inputs_ngc5824.dat")


inputs = normalization_2sigma(inputs0)


m = 50
n = 50
dim = inputs.shape[1]
print (inputs.shape)
n_intr = 2


flag = 0

som = SOM(m, n, dim, n_intr, flag)


som.train(inputs)


w = som.get_weights()
u = som.cal_u_matrix()

np.save("w_gc.npy", w)

np.save("u_gc.npy", u)

print (u)


map_gc, d_gc = som.map_vects(inputs)



print (map_gc.shape)


np.save("map_gc.npy", map_gc)

np.save("d_vw_gc.npy", d_gc)

print (map_gc[:50,0])

print (os.getcwd())
