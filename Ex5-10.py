import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

def NonHarmonic():
	#prefactor of the integral
	A = np.sqrt(8)

	N = 20
	x_i = 0.0
	x_f = 0.0
	xp = 0.0
	wp = 0.0

	#Weights and Points of Gaussian Quadrature
	x, w = gaussxw(N)

	#Scaled Range of x-Points and Weights


	#Range of Amplitude:
	Amp = np.linspace(0, 2, 20)

	#Period Integral Points Array
	T_p = []

	#Period Integral for Each Point
	T_k = 0

	for i in range(N):
		x_f = Amp[i]
		T_k = 0
		for k in range(N):
			xp = 0.5*(x_f-x_i)*x + 0.5*(x_f-x_i)
			wp = 0.5*(x_f-x_i)*w
			T_k += wp[k]*A*f(Amp[i], xp[k])
		T_p.append(T_k)


	plt.plot(Amp, T_p, "k--")
	plt.xlabel("Amplitude (m)")
	plt.ylabel("T (s)")
	plt.savefig("Ex5-10.png")
	
def f(A, X):
	return 1/np.sqrt(A**4 - X**4)

if __name__ == "__main__":
	NonHarmonic()