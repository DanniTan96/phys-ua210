import numpy as np 
import matplotlib.pyplot as plt


def plotter():
	x = np.sort(np.random.uniform(-10, 10, 1000))
	mean = 0
	std = 3.0

	y = (1/(std*np.sqrt(2*np.pi)))*np.exp(-0.5*((x/std)**2))

	plt.plot(x, y, 'bo')
	plt.xlabel("X")
	plt.ylabel("Y")
	# plt.savefig("gaussian.png")
	plt.show()

if __name__ == "__main__":
	plotter()