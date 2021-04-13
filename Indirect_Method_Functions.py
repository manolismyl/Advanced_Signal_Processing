import cmath
import numpy as np
from scipy import signal


def split_sample(N, M, X):
    Y = [0] * N
    for k in range(0, N, M):
        y = X[k:k+M]
        Y[k:k+M] = y - np.mean(y)
    return Y


def r_calculation(x, L, M):
    r = np.zeros(shape=(L,L))
    for t2 in range(L):
        for t1 in range(t2):
            for l in range(0, (M-1-t2)):
                r[t1][t2] += x[l]*x[l+t1]*x[l+t2]
    return r


def get2Dwindow(parzen, L):
    if parzen == 0:
        window = signal.windows.boxcar(L)
        window2D = np.outer(window, window)
        window2D = np.sqrt(window2D)
    else:
        window = signal.windows.parzen(L)
        window2D = np.outer(window, window)
        window2D = np.sqrt(window2D)
    return window2D


def indirect_bispectrum_calculation(c, L, parzen):
    C = np.zeros(shape=(L,L),dtype=complex)
    window2D = get2Dwindow(parzen, L)
    for omega2 in range(L):
        for omega1 in range(L):
            for t2 in range(L):
                for t1 in range(t2):
                    temp = -1j*(omega1*t1 + omega2*t2)
                    temp2 = cmath.exp(-1j)
                    C[omega1][omega2] += c[t1][t2]*window2D[t1][t2]*cmath.exp(temp)
    return C

