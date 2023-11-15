import numpy as np 
import timeit
import matplotlib.pyplot as plt 

def MatrixMult():
	steps = np.arange(10, 510, 10)

	#Time stamps for how long each operation took using for-loops:
	timeZ_for = []

	#Time stamps for how long each operation took using dot():
	timeZ_dot = []

	#Starting time for each operation:
	start_t = 0

	for N in steps:
		start_t = timeit.default_timer()

		C = np.zeros([N, N], float)
		A = np.ones([N, N], float)
		B = np.ones([N, N], float)

		for i in range(N):
			for j in range(N):
				for k in range(N):
					C[i, j] += A[i, k] * B[k, j]

		end_for = timeit.default_timer() - start_t

		timeZ_for.append(end_for)

	start_t = 0

	for N in steps:
		start = timeit.default_timer()

		A = np.ones([N, N], float)
		B = np.ones([N, N], float)

		C = np.dot(A, B)

		end_dot = timeit.default_timer() - start_t

		timeZ_dot.append(end_dot)


	plt.plot(steps, timeZ_for, "b.", label = "For-Loop method")
	plt.plot(steps, timeZ_dot, "r.", label = "dot() method")
	plt.xlabel("# of Elements in Dimension")
	plt.ylabel("Time (s)")
	plt.legend(loc = "best")
	plt.savefig("Exmp4-3-MatrixProduct.png")

if __name__ == "__main__":
	MatrixMult()