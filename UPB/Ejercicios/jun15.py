import numpy as np

matriz = [
#    0 1 2
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matriz1 = [
#    0 1 2
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matriz_np = np.array(matriz)
print(np.sum(matriz))
print(np.sum(matriz,axis = 1))
print(np.concatenate((matriz,matriz1),axis = 0))
print(np.concatenate((matriz,matriz1),axis = 1))