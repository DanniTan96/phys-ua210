import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as optimize

def Y(x):
	return (x - 0.3)**2 * np.exp(x)

def parabolic_step(func=None, a=None, b=None, c=None):
    """returns the minimum of the function as approximated by a parabola"""
    fa = func(a)
    fb = func(b)
    fc = func(c)
    denom = (b - a) * (fb - fc) - (b -c) * (fb - fa)
    numer = (b - a)**2 * (fb - fc) - (b -c)**2 * (fb - fa)
    # If singular, just return b 
    if(np.abs(denom) < 1.e-15):
        x = b
    else:
        x = b - 0.5 * numer / denom
    return(x)

def parabolic_minimize(func=None, astart=None, bstart=None, cstart=None,
                       tol=1.e-5, maxiter=10000):
    a = astart
    b = bstart
    c = cstart
    bold = b + 2. * tol
    niter = 0
    while((np.abs(bold - b) > tol) & (niter < maxiter)):
        bold = b
        b = parabolic_step(func=func, a=a, b=b, c=c)
        if(b < bold):
            c = bold
        else:
            a = bold
        step = np.array([bold, b])
        niter = niter + 1
    return(b)

def golden(func=None, astart=None, bstart=None, cstart=None, tol=1.e-5):
	gsection = (3. - np.sqrt(5)) / 2
	a = astart
	b = bstart
	c = cstart
	while(np.abs(c - a) > tol):
	    # Split the larger interval
	    if((b - a) > (c - b)):
	        x = b
	        b = b - gsection * (b - a)
	    else:
	        x = b + gsection * (c - b)
	    fb = func(b)
	    fx = func(x)
	    if(fb < fx):
	        c = x
	    else:
	        a = b
	        b = x 
	return(b)

# def BrentWiki(func=None, astart=None, bstart=None, tol=1.e-5):
# 	"""Algorithm for Brent's method from Wikipedia"""
# 	a = astart
# 	b = bstart
# 	fa = func(a)
# 	fb = func(b)
# 	s = 0.0
# 	c = 0.0

# 	if (fa*fb) <= 0:
# 		if np.abs(fa) < np.abs(fb):
# 			a = bstart
# 			b = astart
# 			c = a
# 	fc = func(c)

# 	while ((fb != 0) & (np.abs(b-a) > tol)):
# 		if ((fa==fb) & (fb==fc)):
# 			s = b - (fb * ((b-a) / (fb-fa)))
# 		elif (s > ((3.*a + b)/4)) & (s < b):
# 			s = (a+b)/2
# 		fs = func(s)
# 		d = c 
# 		if (fa*fs) < 0:
# 			b = s 
# 		else:
# 			a = s 
# 		break
# 	print(b)

def BrentMe(func=None, astart=None, bstart=None, cstart=None, tol=1.e-5):
	gsection = (3. - np.sqrt(5)) / 2
	a = astart
	b = bstart
	c = cstart
	bold = b + 2. * tol
    niter = 0
    while((np.abs(bold - b) > tol) & (niter < maxiter) & (parabolic_step(func=func, a=a, b=b, c=c) < np.abs(c-a))):
        bold = b
        b = parabolic_step(func=func, a=a, b=b, c=c)
        if(b < bold):
            c = bold
        else:
            a = bold
        step = np.array([bold, b])
        niter = niter + 1
    
    Min = golden(func=func, astart=a, bstart=b, cstart=c)


def plotter():
	x = np.linspace(-1., 1., 100000)
	plt.plot(x, Y(x))
	plt.xlabel("X")
	plt.ylabel("f(x)")
	plt.savefig("PS7_1.png")

parabolic_minimize(func=Y, astart=-0., bstart=0.5, cstart=4.)
golden(func=Y, astart=-10., bstart=0., cstart=10.)
BrentWiki(func=Y, astart=0., bstart=1.)
plotter()
BrentMe(func=Y, astart=-1., bstart=0., cstart=1.)





