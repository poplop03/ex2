#perceptron neural network

import numpy as np

learning_spd = 0.1
x1 =  1
x2 = 0.2 
e = 0 
n = 1
k = 1 


mat1 = [[1,2],[3,4]]
mat2 = [[2,4],[3,6]]


matA = np.matrix('1 2; 3 4')
matB = np.matrix('2 4; 3 6')


def perceptron_nn():
    print("perceptron start")


print(matA*matB)