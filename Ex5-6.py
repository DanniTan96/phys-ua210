import numpy as np 
import matplotlib.pyplot as plt

def TrapInt():
	#Start and End points
	a = 0
	b = 2

	#Number of Slices and Width
	N1 = 10
	N2 = 20
	d1 = (2/N1)
	d2 = (2/N2)

	I1 = 0.5*d1*(f(a) + f(b))
	I2 = 0.5*d2*(f(a) + f(b))

	for k in range(0, N1):
		I1 += d1*f(a + k*d1)

	for k in range(0, N2):
		I2 += d2*f(a + k*d2)

	e2 = (1/3)*(I2 - I1)

	print(I1)
	print(I2)
	print(e2)



	x = np.linspace(0.6, 1., 1000)
	x_ = np.array([0.6, 0.8, 1.])

	plt.plot(x, f(x), 'r', label = r"$f(x)$")
	plt.plot(x_, f(x_), 'b-', label = "Sample Points")
	plt.xlabel("x")
	plt.ylabel("f(x)")
	plt.legend(loc = "upper left")
	plt.savefig("Ex5-6.png")

def f(x):
	return x**4 - 2*x + 1

if __name__ == "__main__":
	TrapInt()
