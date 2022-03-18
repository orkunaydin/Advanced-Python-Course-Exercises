import numpy as np

N = 250

# NxN matrix
X = np.random.randint(100, size=(N,N), dtype=int )

# Nx(N+1) matrix
Y = np.random.randint(100, size=(N,N+1), dtype=int )

# iterate through rows of X
@profile
def matmult(X,Y):
    result = np.matmul(X,Y)
    return result

matmult(X,Y)
