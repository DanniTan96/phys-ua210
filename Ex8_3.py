import numpy as np 
import matplotlib.pyplot as plt

Sigma = 10
R = 28
B = 8./3.

def f(r):
    x = r[0]
    y = r[1]
    z = r[2]
    fx = Sigma*(y-x)
    fy = R*x - y - x*z
    fz = x*y - B*z
    return np.array([fx, fy, fz], float)

a = 0.0
b = 50.0
N = 10000
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
ypoints = []
zpoints = []

r = np.array([0.,1.0, 0.], float)

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1) 
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    r += (k1+2*k2+2*k3+k4)/6

plt.figure(1)
plt.plot(tpoints, ypoints, '--b', label='y(t)')
plt.xlabel('Time (s)')
plt.ylabel('Y-coordinate')
plt.legend(loc='best')
plt.savefig('Ex8_3_YofT.png')

plt.figure(2)
plt.plot(xpoints, zpoints, '--k', label='z(x)')
plt.xlabel('X-coordinate')
plt.ylabel('Z-coordinate')
plt.legend(loc='best')
plt.savefig('Ex8_3_ZofX.png')



