import numpy as np 
import matplotlib.pyplot as plt
from random import random

def decayER():
	#Initial number of atoms for each element:
	Bi213_init = 10000
	Pb_init = 0
	Tl_init = 0
	Bi209_init = 0

	#Half lives in seconds:
	Bi213_hlf = 46*60
	Pb_hlf = 3.3*60
	Tl_hlf = 2.2*60

	#Probabilities of decay:
	P_Bi213_Pb = 0.9791 
	P_Bi213_Tl = 0.0209 
	P_Bi213_ = 1 - 2**(-1/Bi213_hlf)
	P_Pb_Bi209 = 1 - 2**(-1/Pb_hlf)
	P_Tl_Pb = 1- 2**(-1/Tl_hlf)

	#Maximun Time:
	tmax = 20000

	#Time Stamps:
	t_points = np.arange(0, tmax, 1)

	#New number of atoms:
	Bi213_points = []
	Pb_points = []
	Tl_points = []
	Bi209_points = []

	for t in t_points:

		Bi213_points.append(Bi213_init)
		Pb_points.append(Pb_init)
		Tl_points.append(Tl_init)
		Bi209_points.append(Bi209_init)

		decay = 0

		for i in range(Pb_init):
			if random() < P_Pb_Bi209: 
				decay += 1
		Pb_init -= decay
		Bi209_init += decay

		decay = 0

		for j in range(Tl_init):
			if random() < P_Tl_Pb: 
				decay += 1
		Tl_init -= decay 
		Pb_init += decay 

		decay_to_Pb = 0
		decay_to_Tl = 0

		for k in range(Bi213_init):
			if random() < P_Bi213_:
				if random() < P_Bi213_Pb: 
					decay_to_Pb += 1
				else:
					decay_to_Tl += 1
		Bi213_init -= (decay_to_Pb + decay_to_Tl)
		Pb_init += decay_to_Pb
		Tl_init += decay_to_Tl


	plt.plot(t_points, Bi213_points, "b.", label = "Bismuth-213")
	plt.plot(t_points, Pb_points, "r.", label = "Lead-209")
	plt.plot(t_points, Tl_points, "y.", label = "Thallium-209")
	plt.plot(t_points, Bi209_points, "c.", label = "Bismuth-209")
	plt.xlabel("Time (s)")
	plt.ylabel("Number of Atoms")
	plt.legend(loc = "center right")
	plt.savefig("Ex10-2-decayER.png")

if __name__ == "__main__":
	decayER()