import numpy as np
import matplotlib.pyplot as plt

def relaxation(v, r, z, h):
    if r > 0:
        v[r,h] = (v[r+1,z]+v[r-1,z]+v[r,z+1]+v[r,z-1])/4 + h*(v[r+1,z]-v[r-1,h])/(8*r)
    else:
        v[r,h] = (4*v[h,z]+v[r,h+1]+v[r,z-1])
    
if __name__ == '__main__':
    Vx, Vy = np.meshgrid(np.arange(1,10,0.1),np.arange(1,10,0.1))
    print(Vx, Vy)