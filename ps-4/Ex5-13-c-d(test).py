import numpy as np 
from math import factorial
import matplotlib.pyplot as plt 
from gaussxw import gaussxw
from scipy import special

def H(n, x, N):
	H = np.zeros([n+1, N]) #n+1 (i) rows TIMES size_x (j) columns
	H[0, :] = 1

	for j in range(N):
		for i in range(1, n):
			H[i+1, j] = (2*x[j]*H[i, j] - 2*i*H[i-1, j]) * (1 / np.sqrt((2**i)*factorial(i)*np.sqrt(np.pi)))
	#returns 2D array of Hermite Polynoms and Coefficients
	return H


def Psi_5_Gauss():
	n = 5
	N = 100

	#sample points and weights
	xp, wp = gaussxw(N)

	#sample points scaled to infinity
	xp_ = xp / (1-xp**2)

	#2D array of Hermite Polynoms and Coefficients evaluated for xp_
	F = H(n, xp_, N)

	#Remaining part of Psi_5(x) at n = 5 to be integrated
	f_residual = ((xp**2 + xp**4)/((1-xp**2)**4)) * np.exp(-(xp_**2))

	Psi_5 = F[5, :]**2 * f_residual

	Px = wp * Psi_5 

	I = np.sum(Px)

	print(np.size(F))


def Psi_5_GaussHermite():
	n = 5
	N = 100

	#sample points and weights
	xp, wp = special.roots_hermite(N)

	#sample points scaled to infinity
	xp_ = xp / (1-xp**2)

	#2D array of Hermite Polynoms and Coefficients evaluated for xp_
	F = H(n, xp_, N)

	#Remaining part of Psi_5(x) at n = 5 to be integrated
	f_residual = ((xp**2 + xp**4)/((1-xp**2)**4)) * np.exp(-(xp_**2))

	Psi_5 = F[5, :]**2 * f_residual

	Px = wp * Psi_5 

	I = np.sum(Px)

	print(I**0.5)

	

if __name__ == "__main__":
	Psi_5_Gauss()
	Psi_5_GaussHermite()
