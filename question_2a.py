import numpy as np
import matplotlib.pyplot as plt

def relaxation(v, r, z, h):
    if r > 0:
        v[r,z] = (v[r+1,z]+v[r-1,z]+v[r,z+1]+v[r,z-1])/4 + h*(v[r+1,z]-v[r-1,1])/(8*r)
    else:
        v[r,1] = (4*v[1,z]+v[r,z+1]+v[r,z-1])/6
    
if __name__ == '__main__':
    V = np.eye(10)
    for n in range(0, 5):
        for i in range(1, len(V)-1):
            for j in range(1, len(V[i])-1):
                relaxation(V, i, j, 0.1,)
    plt.matshow(V)
    plt.show()