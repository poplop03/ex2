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


result = [[0,0],[0,0]]

def perceptron_nn():
    print("perceptron start")


# def multiply_2x2_vec():
#     for i in range 2:
#         for j in range 2:
#             result[i][j] = mat1[i][]


print(matA*matB)