import numpy as np
import matplotlib.pyplot as plt

def relaxation(v, r, z, h):
    if r > 0:
        return (v[r+1,z]+v[r-1,z]+v[r,z+1]+v[r,z-1])/4 + h*(v[r+1,z]-v[r-1,h])/(8*r)
    else:
        pass
    
if __name__ == '__main__':
    pass