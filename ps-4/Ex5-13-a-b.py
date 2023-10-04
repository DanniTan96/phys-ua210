import numpy as np 
from math import factorial
import matplotlib.pyplot as plt 
from gaussxw import gaussxw


def H(n, x, size_x):
	H = np.zeros([n+1, size_x]) #n+1 (i) rows TIMES size_x (j) columns
	H[0, :] = 1
	x = np.linspace(-x, x, size_x) #size_x indices j from 0 to size_x -1 
	H[1, :] = H[1, :] + 2*x

	for j in range(size_x):
		for i in range(1, n):
			H[i+1, j] = (2*x[j]*H[i, j] - 2*i*H[i-1, j]) * (1 / np.sqrt((2**i)*factorial(i)*np.sqrt(np.pi)))

	return H, x 

def test():
	#F is an n+1 rows by size_x columns 2D array
	n = 30
	x = 4
	size_x = 1000
	F, x = H(n, x, size_x)

	x_30 = (x*10)/4

	Psi_x = np.exp((-x**2)/2)

	for i in range(0, n+1):
		F[i, :] = F[i, :] * Psi_x

	plt.figure(1)
	plt.plot(x, F[0, :], "b--", label = "n = 0")
	plt.plot(x, F[1, :], "g--", label = "n = 1")
	plt.plot(x, F[2, :], "r--", label = "n = 2")
	plt.plot(x, F[3, :], "c--", label = "n = 3")
	plt.plot(x, F[4, :], "m--", label = "n = 4")
	plt.plot(x, F[5, :], "y--", label = "n = 5")
	plt.plot(x, F[6, :], "k--", label = "n = 6")
	plt.xlabel("X (m)")
	plt.ylabel(r"$\psi_n(x)$")
	plt.legend(loc = "best")
	plt.savefig("Ex5-13(a).png")


	plt.figure(2)
	plt.plot(x_30 , 1e+100*F[30, :], "b--", label = "n = 30")
	plt.xlabel("X (m)")
	plt.ylabel(r"$\psi_{30}(x)$")
	plt.legend(loc = "best")
	plt.savefig("Ex5-13(b).png")

if __name__ == "__main__":
	test()








