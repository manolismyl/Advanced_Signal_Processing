from Indirect_Method_Functions import *
import math

lamda1 = 0.12
lamda2 = 0.3
lamda3 = lamda1 + lamda2
lamda4 = 0.19
lamda5 = 0.17
lamda6 = lamda4 + lamda5

lamda = np.array([lamda1, lamda2, lamda3, lamda4, lamda5, lamda6])

N: int = 8192
K = 32
M = 256
L = 64
X = [0]*N

for k in range(N):
    phi = np.random.uniform(0, 2*math.pi, 6)
    phi[2] = phi[0] + phi[1]
    phi[5] = phi[3] + phi[4]
    x = [0]*len(phi)
    for i in range(len(phi)):
        x[i] = math.cos(2*math.pi*lamda[i] + phi[i])
    X[k] = sum(x)


Y = split_sample(N, M, X)

c = np.zeros(shape=(L, L))
for k in range(0, N, M):
    r = r_calculation(Y[k:k+M], L, M)
    c += r
c = c/K
C_indirect = indirect_bispectrum_calculation(c, L, 0)







