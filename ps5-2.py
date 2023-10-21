import numpy as np 
import matplotlib.pyplot as plt
import numpy.linalg as linalg
import pandas as pd

df = pd.read_csv("signal.dat", delimiter='|', header=0, names=['1', 'time', 'signal', '3'])
T = np.array(df['time'])
S = np.array(df['signal'])

def data_plot():
	plt.plot(T, S, 'b.', label = 'Data')
	plt.xlabel('Time (s)')
	plt.ylabel('Signal (signal unit)')
	plt.legend(loc = 'upper left')
	plt.savefig('ps5-2-Data.png')

def svd_P3Fit():
	N = 3
	A = np.zeros((len(T), N+1))

	for i in range(N+1):
		A[:, i] = T**i

	(u, w, vt) = np.linalg.svd(A, full_matrices=False)
	winv = np.zeros((N+1, N+1))

	for i in range(N+1):
		if w[i] > 0:
			winv[i, i] = 1. / w[i]
		else:
			winv[i, i] = 0.

	Ainv = vt.transpose().dot(winv).dot(u.transpose())

	c = Ainv.dot(S)

	Sm = A.dot(c)

	Res = S - Sm
	ResSq = Res**2

	ResSq_Avg = np.sum(ResSq)/len(ResSq)
	Res_Avg_Sq = (np.sum(Res)/len(Res))**2

	sigma = np.sqrt(ResSq_Avg - Res_Avg_Sq)

	print(sigma)

	plt.plot(T, S, 'b.', label = 'Data')
	plt.plot(T, Sm, 'k.', label = 'Model')
	plt.xlabel('Time (s)')
	plt.ylabel('Signal (signal unit)')
	plt.legend(loc = 'upper left')
	plt.savefig('ps5-2-P3Fit.png')

def svd_P9Fit():
	N = 9
	A = np.zeros((len(T), N+1))

	for i in range(N+1):
		A[:, i] = T**i

	(u, w, vt) = np.linalg.svd(A, full_matrices=False)
	winv = np.zeros((N+1, N+1))

	for i in range(N+1):
		if w[i] > 0:
			winv[i, i] = 1. / w[i]
		else:
			winv[i, i] = 0.

	Ainv = vt.transpose().dot(winv).dot(u.transpose())

	c = Ainv.dot(S)

	Sm = A.dot(c)

	Res = S - Sm
	ResSq = Res**2

	ResSq_Avg = np.sum(ResSq)/len(ResSq)
	Res_Avg_Sq = (np.sum(Res)/len(Res))**2

	sigma = np.sqrt(ResSq_Avg - Res_Avg_Sq)

	print(sigma)

	plt.plot(T, S, 'b.', label = 'Data')
	plt.plot(T, Sm, 'k.', label = 'Model')
	plt.xlabel('Time (s)')
	plt.ylabel('Signal (signal unit)')
	plt.legend(loc = 'upper left')
	plt.savefig('ps5-2-P9Fit.png')

def svd_HarmFit():
	dt = max(T)-min(T)

	h = 100
	A = np.zeros((len(T), h+1))

	for n in range(h+1):
		A[:, n] = np.sin(n*T/dt)+np.cos(n*T/dt)

	(u, w, vt) = np.linalg.svd(A, full_matrices=False)
	winv = np.zeros((h+1, h+1))

	for i in range(h+1):
		if w[i] > 0:
			winv[i, i] = 1. / w[i]
		else:
			winv[i, i] = 0.

	Ainv = vt.transpose().dot(winv).dot(u.transpose())

	c = Ainv.dot(S)

	Sm = A.dot(c)

	Res = S - Sm
	ResSq = Res**2

	ResSq_Avg = np.sum(ResSq)/len(ResSq)
	Res_Avg_Sq = (np.sum(Res)/len(Res))**2

	sigma = np.sqrt(ResSq_Avg - Res_Avg_Sq)

	print(sigma)

	plt.plot(T, S, 'b.', label = 'Data')
	plt.plot(T, Sm, 'k.', label = 'Model')
	plt.xlabel('Time (s)')
	plt.ylabel('Signal (signal unit)')
	plt.legend(loc = 'upper left')
	plt.savefig('ps5-2-HarmFit.png')

if __name__ == "__main__":
	data_plot()
	svd_P3Fit()
	svd_P9Fit()
	svd_HarmFit()

