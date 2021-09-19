import numpy as np
zv = []
x = []
n, p = [int(x) for x in input().split()]
for i in range(n):
    a = [float(x) for x in input().split(' ')]
    ab = np.array(a)
    qw = ab.sum()
    zx = qw/p
    zb = round(zx, 2)
    x.append(zb)
    bn = np.array(x)
print (bn)