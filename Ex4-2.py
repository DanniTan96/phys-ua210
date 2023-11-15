import numpy as np

def Quad_Solver():
	a = 1e-3
	b = 1e3
	c = 1e-3

	xa_neg = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
	xa_pos = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)

	print("The First X here is more accurate: " + str(xa_neg) + ", " + str(xa_pos))

	xb_neg = (2*c)/(-b + np.sqrt(b**2 - 4*a*c))
	xb_pos = (2*c)/(-b - np.sqrt(b**2 - 4*a*c))
	

	print("The Second X here is more accurate: " + str(xb_neg) + ", " + str(xb_pos))

	xc_neg = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
	xc_pos = (2*c)/(-b - np.sqrt(b**2 - 4*a*c))
	
	print("Then the Best X's are" + " = " + str(xc_neg) + ", and " + str(xc_pos))


if __name__ == "__main__":
	Quad_Solver()
