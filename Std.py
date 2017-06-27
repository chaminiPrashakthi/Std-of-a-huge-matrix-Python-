#imported files 
import csv
import numpy as np
import math
#read csv file and convert it in to an array
csv= np.genfromtxt
csv = np.genfromtxt('Std.csv',delimiter=",")
#print csv
#get number of raws
N=len(csv[:])
#print N
#X is x bar which is the mean of each column
X = np.mean(csv,axis=0)
#print X
sum = 0

for i in range(N):
	for j in range(len (X[:])):
		val= csv[i,j]-X[j]
		squre = val**2
		sum = sum+ squre
#print sum

final = sum/(N-1)
#print final
print math.sqrt(final)

	
