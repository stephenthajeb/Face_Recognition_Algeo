from gmpy2 import *
import numpy as np

# Inisiasi precision
get_context().precision = 100

def scalar(u):
	sqrscalar = 0
	for i in range(len(u)):
		sqrscalar += pow(u[i],2)
	return sqrt(sqrscalar)

def CosineSimilarity(u, v):
	dotProduct = 0
	assert(len(u)==len(v))
	for i in range(len(u)):
		dotProduct += u[i]*v[i]
	return div(dotProduct,mul(scalar(u),scalar(v)))

def CosineSimilarityMat(M1, M2):
	M = []
	for i in range(len(M1)):
		M.append(1-CosineSimilarity(M1[i],M2[0]))
	return np.array(M)