import numpy as np 
from math import factorial
import matplotlib.pyplot as plt 
from gaussxw import gaussxw
from scipy import special

def H(n, x, N): 	#returns 2D array of Hermite Polynoms
	H = np.zeros([n+1, N]) #n+1 (i) rows TIMES size_x (j) columns
	H[0, :] = 1
	H[1, :] = H[1, :] + 2*x

	for j in range(N):
		for i in range(1, n):
			H[i+1, j] = (2*x[j]*H[i, j] - 2*i*H[i-1, j])

	return H


def Psi_5_Gauss():
	n = 5
	N = 100
	#sample points
	z, w = gaussxw(N)
	x = z / (1-z**2)

	#Hermite Polynoms at corresponding n, x values. Size n rows by N columns
	HP = H(n, x, N)

	#Hermite Polynoms at n = 5
	HP_5 = HP[5, :]

	#Static Normalization Constant for n = 5
	S_5 = 1 / ((2**5) * factorial(5) * np.sqrt(np.pi))
	
	#Remaining of Integrand
	G = (z**2 + z**4)/((1-z**2)**4) * np.exp(-(x**2))

	#Function evaluations
	E = G * (HP_5**2)

	#Weighted Evaluations--Scaled Integrand--
	I = w * E 

	rms_G = np.sqrt(np.sum(I) * S_5)

	print(rms_G)

def Psi_5_GaussHermite():
	n = 5
	N = 100
	#sample points
	zp, wp = special.roots_hermite(N)
	xp = zp / (1-zp**2)

	#Hermite Polynoms at corresponding n, x values. Size n rows by N columns
	HPp = H(n, xp, N)

	#Hermite Polynoms at n = 5
	HPp_5 = HPp[5, :]

	#Static Normalization Constant for n = 5
	S_5 = 1 / ((2**5) * factorial(5) * np.sqrt(np.pi))
	
	#Remaining of Integrand
	Gp = (zp**2 + zp**4)/((1-zp**2)**4) * np.exp(-(xp**2))

	#Function evaluations
	Ep = Gp * (HPp_5**2)

	#Weighted Evaluations--Scaled Integrand--
	Ip = wp * Ep 

	rms_GH = np.sqrt(np.sum(Ip) * S_5)

	print(rms_GH)

if __name__ == "__main__":
	Psi_5_Gauss()
	Psi_5_GaussHermite()
