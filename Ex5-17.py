import numpy as np 
import matplotlib.pyplot as plt 
from gaussxw import gaussxwab	

def Gamma(a, x):
	return x**(a-1) * np.exp(-x)

def Gamma_Int(a, z, x):
	return ((a-1)/((1-z)**2)) * np.exp(((a-1)*np.log(x))-x)

def Int_Plot():
	x = np.linspace(0, 5, 1000)
	a = np.array([2, 3, 4])

	I_arr = np.zeros([3, 1000])

	for i in range(3):
		I_arr[i] = Gamma(a[i], x)
	
	plt.plot(x, I_arr[0, :], "k--", label = "a = 2")
	plt.plot(x, I_arr[1, :], "b--", label = "a = 3")
	plt.plot(x, I_arr[2, :], "r--", label = "a = 4")
	plt.xlabel("X")
	plt.ylabel("Inegrand")
	plt.legend(loc = "upper left")
	plt.savefig("Ex5-17-a.png")

def Integrator(a):
	N = 1000
	start = 0.0
	stop = 1.0
	c = a - 1 
	z, w = gaussxwab(N, start, stop)

	x = z*c / (1 - z)
	I_ = Gamma_Int(a, z, x)

	I = w * I_

	GammaFin = np.sum(I)

	print(GammaFin)

if __name__ == "__main__":
	Int_Plot()
	for a in np.array([3./2., 3, 6, 10]):
		Integrator(a)
