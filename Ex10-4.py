import numpy as np
import matplotlib.pyplot as plt
from random import random

def smart_decayER():
	tau = 3.053*60

	z = np.ones(1000)

	for i in range(1000):
		z[i] = z[i] * random()

	t = -tau * np.log(1 - z) / np.log(2)

	t_sorted = np.sort(t)

	num_atoms = 1000 - np.arange(0, 1000)

	plt.plot(t_sorted, num_atoms, "y.", label = "# of Thallium-208 atoms")
	plt.xlabel("Time (s)")
	plt.ylabel("Number of Remaining Atoms")
	plt.legend(loc = "upper right")
	plt.savefig("Ex10-4-SmartDecayER.png")

if __name__ == "__main__":
	smart_decayER()