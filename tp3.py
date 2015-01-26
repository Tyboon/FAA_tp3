import numpy as np

x = np.loadtxt("x.txt")
y = np.loadtxt("y.txt")

init = np.ones((x.shape))

x = np.vstack((init,x))

for i in range(2,21) :
	tmp = np.power(x[1],i)
	x = np.vstack((x,tmp))

print x
