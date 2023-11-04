import numpy as np 
import matplotlib.pyplot as plt
import astropy.io.fits
import numpy.linalg as linalg

hdu_list = astropy.io.fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data

def Plotter():
	plt.plot(flux[0, :], 'k', label = 'Galaxy 1')
	plt.plot(flux[1, :], 'b', label = 'Galaxy 2')
	plt.plot(flux[2, :], 'r', label = 'Galaxy 3')
	plt.plot(flux[3, :], 'c', label = 'Galaxy 4')
	plt.plot(flux[4, :], 'y', label = 'Galaxy 5')
	plt.legend(loc = 'best')
	plt.xlabel(r'Wavelength ($\AA$)')
	plt.ylabel(r'Flux ($10^{-17}erg$ $s^{-1} cm^{-2}$)')
	plt.savefig('Plot5GalaxFlux.png')

def Normalizer():
	Int = np.zeros(9713)
	norm_flux = flux
	for i in range(9713):
		Int[i] = np.sum(flux[i, :])
		norm_flux[i, :] = flux[i, :] / Int[i]
	return norm_flux


def Meaner():
	norm_flux = Normalizer()
	res_flux = norm_flux
	mean = np.zeros(9713)
	for i in range(9713): 
		mean[i] = np.sum(norm_flux[i, :]) / 4001.
		res_flux[i, :] = norm_flux[i, :] - mean[i]
	return res_flux

def CMatrixPCA():
	R = Meaner()
	RT = np.transpose(R)
	C = RT.dot(R)
	evals, evecs = linalg.eig(C)
	plt.plot(evecs[0, :], 'k--', label = 'EVector 1')
	plt.plot(evecs[1, :], 'b--', label = 'EVector 2')
	plt.plot(evecs[2, :], 'r--', label = 'EVector 3')
	plt.plot(evecs[3, :], 'c--', label = 'EVector 4')
	plt.plot(evecs[4, :], 'y--', label = 'EVector 5')
	plt.legend(loc = 'best')
	plt.savefig('Plot5EigVecPCA.png')

def CMatrixSVD():
	R = Meaner()
	(U, w, VT) = linalg.svd(R)
	V = np.transpose(VT)
	plt.plot(V[0, :], 'k--', label = 'EVector 1')
	plt.plot(V[1, :], 'b--', label = 'EVector 2')
	plt.plot(V[2, :], 'r--', label = 'EVector 3')
	plt.plot(V[3, :], 'c--', label = 'EVector 4')
	plt.plot(V[4, :], 'y--', label = 'EVector 5')
	plt.legend(loc = 'best')
	plt.savefig('Plot5EigVecSVD.png')
	
if __name__ == "__main__":
	CMatrixPCA()
	CMatrixSVD()














