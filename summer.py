import numpy as np
import timeit

def summer():
	start = timeit.default_timer()
	V_t = 0
	L = 1000

	for i in range(-L, L):
			
		for j in range(-L, L):
	
			for k in range(-L, L):
				if i == 0 and j==0 and k==0:
					continue
				d = (i+j+k)%2
				V_t += (-1)**d * (1/np.sqrt(i**2 + j**2 + k**2))
	end = timeit.default_timer() - start
	print(V_t)
	print(end)



if __name__ == "__main__":
	summer()