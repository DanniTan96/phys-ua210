import numpy as np 
import matplotlib.pyplot as plt

def looper():
	N = 1000
	x = np.linspace(-2, 2, N)
	y = np.linspace(-2, 2, N)

	c = x[ : , np.newaxis] + 1j*y

	grid = np.zeros((N, N))

	for i in range(N):
		for j in range(N):
			z = 0
			n = 0
			this_c = c[i , j]
			while n < 100:
				n += 1
				z = np.real(z**2) + np.real(this_c) + 1j*(np.imag(z**2) + np.imag(this_c))
				if checker(z) == True:	
					grid[j, i] = n
					n = 101

	plt.imshow(grid)
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.jet()
	plt.colorbar(label="n")
	plt.savefig("Mandlebrot.png")


def checker(z):
	if np.abs(z) > 2:
		return True
	else:
		return False


if __name__ == "__main__":
	looper()


