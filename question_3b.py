import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    h, r = 1.5, 1.5

    # a, b = (2*r+h)/(8*r), (2*r-h)/(8*r)

    # Q = np.array([
    #     [0, 1/4, 0, 0, 0, 0, 0, 0],
    #     [1/4, 0, 1/4, 0, 0, 0, 0, 0],
    #     [0, 1/4, 0, 1/4, 0, 0, 0, 0],
    #     [0, 0, 1/4, 0, 1/4, 0, 0, 0],
    #     [0, 0, 0, 1/4, 0, 1/4, 0, 0],
    #     [0, 0, 0, 0, 1/4, 0, b, 0],
    #     [0, 0, 0, 0, 0, 2/3, 0, 1/6],
    #     [0, 0, 0, 0, 0, 0, 1/6, 0]
    #     ])
    
    # R = np.array([
    #     [0, 0, 0, 0, b, 0, 1/4, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    #     [0, 0, 0, b, 0, 0, 0, 0, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    #     [0, 0, b, 0, 0, 0, 0, 0, 0, 0, a, 0, 0, 0, 0, 0, 0, 0, 0,],
    #     [0, b, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, 0, 0, 0, 0, 0, 0, 0,],
    #     [b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, 0, 0, 0, 0, 0, 0,],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/4, 0,],
    #     [1/6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2/3, 1/6,]
    #     ])
    
    # N = np.linalg.inv(np.eye(8)-Q)

    # B = np.matmul(N, R)

    # Vr = np.array([0, 0, 0, 0, 0, 0, 0, -300, -300, -300, -300, -300, -300, -300, -300, -300, -300, -300, -300,])

    # Vt = B*Vr
    # # V = np.array([
    # #     [Vt[1,23], Vt[1,22], Vt[1,21], Vt[1,20], Vt[1,19], Vt[1,18], Vt[1,17], Vt[1,16], Vt[1,17]]])
    # print(Vt.shape)
    # plt.imshow(Vt)
    # plt.show()

    P = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, (2*r-h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, (2*r-h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, (2*r-h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, (2*r-h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 1, 1/6, 0, 0, 0, 0, 0, 0, 0, (2*r-h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 1/6, 0, 0, 0, 0, 0, 0, 0, (2*r-h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 1/6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 1/6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 2/3, 0, 0, 0, 0, 0, 0, 0, 1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 2/3, 0, 0, 0, 0, 0, 0, 0, 1/4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (2*r+h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (2*r+h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (2*r+h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (2*r+h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (2*r+h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (2*r+h)/(8*r), 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,]
        ])

    Vr = -300

    V = np.array([[0, 0, 0, 0, 0, 0, .5, .5, Vr,
                  0, .5, .5, .5, .5, .5, .5, Vr, Vr, 
                  Vr, Vr, Vr, Vr, Vr, Vr, Vr, Vr, Vr,]]).transpose()
    

    for i in range(0, 1000):
        V = np.matmul(P, V)

    plt.contourf(V.reshape(3,9), levels=50, cmap='inferno')
    plt.show()