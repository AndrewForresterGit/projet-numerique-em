import numpy as np
import matplotlib.pyplot as plt

def relaxation(v, r, z, h, A):
    if A:
        if r > 0:
            v[r,z] = (v[r+1,z]+v[r-1,z]+v[r,z+1]+v[r,z-1])/4 + h*(v[r+1,z]-v[r-1,1])/(8*r)
        else:
            v[r,z] = (4*v[r,z]+v[r,z+1]+v[r,z-1])/6


if __name__ == '__main__':
    V = np.ndarray((30,120), dtype=float)
    M = np.full((30,120), True, dtype=bool)

    # conditions frontières
    M[:,:] = True
    V[:,0], M[:,0] = 0, False
    V[0,:75], M[0,:75] = 0, False
    V[-1,:], M[-1,:] = 1, False

    x, y = np.meshgrid(np.arange(0, 120, 1), np.arange(0, 30, 1))
    V, M = np.where(x + y > 118, 1, V), np.where(x + y > 118, False, M)

    for n in range(0, 1000):
        for i in range(0, len(V)-1):
            for j in range(0, len(V[i])-1):
                relaxation(V, i, j, 0.1, M[i,j])
    V = np.where(x + y > 119, np.NaN, V)

    fig = plt.figure()
    ax = fig.subplots()
    ax.contourf(x, y, V, levels=100)
    plt.show()