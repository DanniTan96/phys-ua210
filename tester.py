import numpy as np 
import numpy.ma as ma
import matplotlib.pyplot as plt
from gaussxw import gaussxw

def test():
	N = 
	a = 0.0
	b = 2.0

	#Weights and Points of Gaussian Quadrature
	x, w = gaussxw(N)

	#Scaled Range
	xp = 0.5*(b-a)*x + 0.5*(b-a)
	wp = 0.5*(b-a)*w

	#Integral
	s = 0.0
	for k in range(N):
		s += wp[k]*f(xp[k])

	print(s)

def f(x):
	return x**4 - 2*x + 1







	
	# n = 5
	# N = 100

	# #sample points and weights
	# z, w = gaussxw(N)

	# #sample points scaled to infinity
	# x = z / (1-z**2)

	# #2D array of n by N of "Normalized" Hermite Polynoms for each Energy Level n,
	# #evaluated at x[N]
	# F = H(n, z, N)

	# #Remaining part of Psi_5(x) at n = 5 to be integrated
	# f_residual = ((1 + xp**2)/((1-xp**2)**2)) * xp_**2 * np.exp(-(xp_**2)/2)

	# Psi_5 = F[5, :] * f_residual

	# Psi_5_Sq = Psi_5**2

	# Px = wp * Psi_5_Sq

	# I = np.sum(Px)

	# print(I**0.5)


if __name__ == "__main__":
	test()