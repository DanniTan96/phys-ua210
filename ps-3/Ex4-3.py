import numpy as np 
import matplotlib.pyplot as plt 

def deriv():
	x = np.ones(7)
	delta = np.array([1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14], dtype = np.float32)

	deriv_real = np.ones(7) 

	deriv = (f(x + delta) - f(x))/delta

	error = np.abs(deriv_real - deriv)

	vert = np.log10(error)
	horiz = np.log10(delta)

	plt.plot(horiz, vert, "ko")
	plt.xlabel(r"$log_{10}(\delta)$")
	plt.ylabel(r"$log_{10}(|Analytic - Computational|)$")
	plt.savefig("Ex4-3.png")

def f(x):
	y = x*(x-1)
	return y


if __name__ == "__main__":
	deriv()