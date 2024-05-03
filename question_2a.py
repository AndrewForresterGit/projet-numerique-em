import numpy as np
import matplotlib.pyplot as plt


def filtre(v, r, z, h, A):
    if A:
        if r > 0:
            v[r,z] = (v[r+1,z]+v[r-1,z]+v[r,z+1]+v[r,z-1])/4 + h*(v[r+1,z]-v[r-1,z])/(8*r)
        else:
            v[r,z] = (4*v[1,z]+v[r,z+1]+v[r,z-1])/6


if __name__ == '__main__':
    V = np.full((31,121), .5, dtype=float)
    M = np.full((31,121), True, dtype=bool)

    M[:,:] = True
    V[:,0], M[:,0] = 0, False
    V[0,:75], M[0,:75] = 0, False
    V[-1,:], M[-1,:] = -300, False

    R, Z = np.arange(0, 31, 1), np.arange(0, 121, 1)
    R1, Z1 = np.meshgrid(Z, R)
    V, M = np.where(R1 + Z1 > 118, -300, V), np.where(R1 + Z1 > 118, False, M)
    
    fig = plt.figure(figsize=(12, 6),layout='constrained')
    ax = fig.subplots()

    for n in range(0, 2500):
        for i in range(0, len(V)):
            for j in range(0, len(V[i])):
                filtre(V, i, j, 0.1, M[i,j])

    V = np.where(R1 + Z1 > 119, np.NaN, V)

    ax.set_xlim(0,120)
    ax.set_ylim(0, 60)
    ax.matshow(np.concatenate((np.flip(V[1:,:], axis=0), V), axis=0), cmap='viridis')
    # ax.contourf(np.concatenate((np.flip(V[1:,:], axis=0), V), axis=0), levels=100, cmap='inferno')
    plt.show()