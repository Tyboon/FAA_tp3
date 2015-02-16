import numpy as np
import matplotlib.pyplot as plt

def chargement (x,y,deg=20) :
	X = np.loadtxt("x.txt")
	Y = np.loadtxt("y.txt")

	X = np.asmatrix(X)
	Y = np.asmatrix(Y)
	init = np.ones((X.shape))

	X = np.vstack((init,X))

	# Enrichissement de l'espace d'hypothese via les polynomes de X
	for i in range(2,deg+1) :
		tmp = np.power(X[1],i)
		X = np.vstack((X,tmp))
	return X,Y

# teta = (XXt)**-1 * (XY)
def calculTheta (x,y) :
	tmp1 = np.dot(x,x.T)
	tmp2 = np.dot(x,y)
	theta = np.dot(tmp1.I, tmp2)
	return theta

# Calcul des theta pour Y et chaque polynome X avec le moindre carre
def calculThetas(X,Y) :
	thetas = [] 
	for i in range(2,X.shape[0]) :
		thetas.append(calculTheta(X[0:i],Y))
	return thetas

# Calcul du polynome avec le theta donnee
def calculPoly(X,theta) :
	degre = theta.shape[0]
	poly = np.zeros(X.shape[0])
	for i in xrange(0,degre) :
		poly += theta.item(i) * X ** (i)
	return poly

# Calcul de tous les polynomes
def calculPolys(X,thetas) :
	res = []
	tmp=[]
	for t in thetas :
		tmp = calculPoly(alea,t)
		res.append(tmp)
	return res

# Estimation du risque reel par validation croisee en K pli
def calculRisqueReel(X,Y,K=10) :
	pass

def dessiner (x,y,a,poly) :
	plt.plot(x,y,'b.')
	plt.plot(a,poly,'r-')
	plt.ylabel('position')
	plt.xlabel('temps')
	plt.show()


if "__main__" == __name__ :
	X,Y = chargement("x.txt","y.txt")
	thetas = calculThetas(X,Y.T)
	alea = np.arange(-2.5,2.6,0.1)
	polys = calculPolys(alea,thetas)
	for poly in polys :
		dessiner(X[1],Y,alea,poly)
