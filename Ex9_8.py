"""
Author: Daniel E. Tanagho
-------------------------
This program solves Exercise 9.8 in Newman:
Solving the Time-Dependent Schrodinger Equation using the
Crank-Nicolson method.
----------------------------------------------------------
"""
import numpy as np 
import matplotlib.pyplot as plt
from numpy.linalg import solve

## Global Constants
m = 9.109e-31                       ## Mass of electron (kg)
L = 1.e-8                           ## Width of square box (m)
x0 = L/2                            ## Initial position (m)
sig = 1.e+10                        ## Gaussian wave packet width (m)
kap = 5.e+10                        ## Wave factor Kappa (m^-1)
h_bar = 1.055e-34                   ## Reduced Planck Constant (J.s)

## Integration Constants
N = 1000                            ## Number of spatial slices
a = L/N                             ## Grid Width (m)
h = 1.e-18                          ## Time Step (s)

## Tridiagonal Array Elements
a1 = 1 + 1.j*(h*h_bar)/(2*m*a**2)   ## Main Diagonal for Matrix A
a2 = -1.j*(h*h_bar)/(4*m*a**2)      ## Upper and Lower Diagonal for Matrix A

b1 = 1 - 1.j*(h*h_bar)/(2*m*a**2)   ## Main Diagonal for Matrix B
b2 = 1.j*(h*h_bar)/(4*m*a**2)       ## Upper and lower Diagonal for Matrix B

## Initial Wavefunction
def Psi_t0(x, x0, sig, kap):
	return np.exp(-(x-x0)**2 / 2*sig**2) * np.exp(1.j * kap * x)

## Psi_t0(x, t=0) at all the grid points, plus all the x grid points
psi0 = np.zeros(N, dtype = 'complex_')
x = np.zeros(N, float)
for i in range(1, N+1):
	psi0[i-1] = Psi_t0((i*a), x0, sig, kap)
	x[i-1] = i*a 

## Tridiagonal Matrices
A = np.zeros([N, N], dtype = 'complex_')
# B = np.zeros([N, N], dtype = 'complex_')
for i in range(N):
	for j in range(N):
		if j == i:
			A[i, j] = a1
		if (j == (i+1)) or (j == (i-1)):
			A[i, j] = a2
# for i in range(N):
# 	for j in range(N):
# 		if j == i:
# 			B[i, j] = b1
# 		if (j == (i+1)) or (j == (i-1)):
# 			B[i, j] = b2

## First Crank-Nicolson Step
v0 = np.zeros(N, dtype = 'complex_')
v0[0] = b1*psi0[0] + b2*psi0[1]
v0[-1] = b2*psi0[-2] + b1*psi0[-1]
for i in range(1, N-1):
	v0[i] = b1*psi0[i] + b2*(psi0[i-1]+psi0[i+1])

## psif is the final N*N array with all the psi values
psif = np.zeros([N, N], dtype='complex_')
psif[0, :] = psi0
psif[1, :] = v0

## Integration Loop
for i in range(2, N):
	psif[i, :] = solve(A, psif[i-1, :])

## Plotting psi at various times. h is the time step indicated above.
plt.plot(x, np.real(psif[0, :]), 'r-', label=r'$\psi(t=0)$')
plt.plot(x, np.real(psif[199, :]), 'm-', label=r'$\psi(t=200h)$')
plt.plot(x, np.real(psif[399, :]), 'y-', label=r'$\psi(t=400h)$')
plt.plot(x, np.real(psif[599, :]), 'g-', label=r'$\psi(t=600h)$')
plt.plot(x, np.real(psif[799, :]), 'b-', label=r'$\psi(t=800h)$')
plt.plot(x, np.real(psif[-1, :]), 'c-', label=r'$\psi(t=1000h)$')
plt.xlabel('Position (m)')
plt.ylabel(r'$\psi(x)$ (Unitless)')
plt.legend(loc = 'best')
plt.show()
# plt.savefig('Ex9_8_RealWaveTimeEvolution.png')

