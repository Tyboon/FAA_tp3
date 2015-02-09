import numpy as np

def chargement (x,y,deg=20) :
	X = np.loadtxt("x.txt")
	Y = np.loadtxt("y.txt")

	init = np.ones((X.shape))

	X = np.vstack((init,X))

	# Enrichissement de l'espace d'hypothese via les polynomes de X
	for i in range(2,deg+1) :
		tmp = np.power(X[1],i)
		X = np.vstack((X,tmp))
	return X,Y

# teta = (XXt)**-1 * (XY)
def calculTheta (x,y) :
	tmp1 = np.asmatrix(np.dot(x,x.T))
	tmp2 = np.dot(x,y)
	theta = np.dot(tmp1.I, tmp2)
	return theta

# Calcul des theta pour Y et chaque polynome X avec le moindre carre
def calculThetas(X,Y) :
	thetas = [] 
	for i in range(1,X.shape[0]) :
		thetas.append(calculTheta(X[0:i],Y))
	return thetas

# Calcul du polynome avec le theta donnee
def calculPoly(X,Y,theta) :
	poly = 0
	degre = len(theta)
	for i in range(1,degre) :
		poly += X[degre] * theta[i]
	return poly

# Calcul de tout les polynomes
def calculPolys(X,Y,thetas) :
	degreMax = X.shape[0]
	res = []
	for i in range(1,degreMax-1) :
		print i
		tmp = calculPoly(X[0:i],Y,thetas[i])
		res.append(tmp)
	return res

# Estimation du risque reel par validation croisee en K pli
def calculRisqueReel(X,Y,K=10) :
	pass


if "__main__" == __name__ :
	X,Y = chargement("x.txt","y.txt")
	thetas = calculThetas(X,Y)
	polys = calculPolys(X,Y,thetas)
	print polys
