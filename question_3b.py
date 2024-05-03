import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    h, r = 1.5, 1.5
    a, b = (2*r+h)/(8*r), (2*r-h)/(8*r)

    Q = np.array([
        [0, 1/4, 0, 0, 0, 0, 0, 0],
        [1/4, 0, 1/4, 0, 0, 0, 0, 0],
        [0, 1/4, 0, 1/4, 0, 0, 0, 0],
        [0, 0, 1/4, 0, 1/4, 0, 0, 0],
        [0, 0, 0, 1/4, 0, 1/4, 0, 0],
        [0, 0, 0, 0, 1/4, 0, b, 0],
        [0, 0, 0, 0, 0, 2/3, 0, 1/6],
        [0, 0, 0, 0, 0, 0, 1/6, 0]
    ])
    
    R = np.array([
        [0, 0, 0, 0, b, 0, 1/4, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, b, 0, 0, 0, 0, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, b, 0, 0, 0, 0, 0, 0, 0, a, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, b, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, 0, 0, 0, 0, 0, 0, 0,],
        [b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, 0, 0, 0, 1/4, 0,],
        [1/6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2/3, 1/6,]
    ])
    Vr = np.array([0, 0, 0, 0, 0, 0, 0, 0, -300, -300, -300, -300, -300, -300, -300, -300, -300, -300, -300,]).transpose()

    N = np.linalg.inv(np.eye(8)-Q)
    B = np.matmul(N, R)
    Vt = np.matmul(B, Vr)

    V = np.array([
        [np.NAN, np.NAN, Vr[13], Vr[12], Vr[11], Vr[10], Vr[9], Vr[8], Vr[7],],
        [np.NAN, Vr[17], Vt[5], Vt[4], Vt[3], Vt[2], Vt[1], Vt[0], Vr[6]],
        [Vr[18], Vt[7], Vt[6], Vr[0], Vr[1], Vr[2], Vr[3], Vr[4], Vr[5],]
    ])

    # V = np.array([
    #    [Vr[7], Vr[8], Vr[9], Vr[10], Vr[11], Vr[12], Vr[13], np.NAN, np.NAN],
    #    [Vr[6], Vt[0], Vt[1], Vt[2], Vt[3], Vt[4], Vt[5], Vr[17], np.NAN],
    #    [Vr[5], Vr[4], Vr[3], Vr[2], Vr[1], Vr[0], Vt[6], Vt[7], Vr[18]]
    # ])

    fig = plt.figure(figsize=(12, 6),)
    ax = fig.subplots()
    
    V = np.concatenate((V, np.flip(V, axis=0)[1:,:]))
    im = ax.imshow(V, extent=[0,13.5,-3,3], cmap='turbo')
    fig.colorbar(im)
    
    for (i, j), z in np.ndenumerate(V):
        print(i,j)
        if z is not np.NAN:
            y = 1.5*i+.75
            if i < 2:
                y = -1.5*i
            ax.text(1.5*j+.75, y, '{:0.1f}'.format(z), ha='center', va='center',
                    bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'),)
            
            
        
    ax.set_xticks(np.arange(0, 13.5, 1.5))
    ax.set_yticks(np.arange(-3, 3, 1.5))
    ax.set_xlabel('z [mm]')
    ax.set_title("Potentiel de la chambre d'ionisation")
    plt.show()
