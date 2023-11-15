import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as optimize


age, recog = np.loadtxt('survey.csv', delimiter=',', skiprows=1, unpack=True)