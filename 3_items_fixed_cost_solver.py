from __future__ import division
import math
import random
from operator import itemgetter

# Example Problem
Xs = [5, 105, 1]
Ys = [10.0, 200.0, 2000.0]


max_rate = (int) (M * max((float)(x)/(float)(y) for (x,y) in zip (Xs, Ys)))
DP = [(float)(M)/(float)(i) for i in xrange(1, max_rate+1)]
DP_path = [0 for i in xrange(1, max_rate+1)]

# Just a placeholder value for -1 so indices match up.
DP.insert(0, -1)
DP_path.insert(0, -1)

for i in xrange(max_rate, 0, -1):
	# Default values so that these won't be the min if they don't get updated
	item1 = DP[i]+1
	item2 = DP[i]+1
	item3 = DP[i]+1

	if i + Xs[0] <= max_rate:
		item1 = (float)(Ys[0])/(float)(i) + DP[i + Xs[0]]
	if i + Xs[1] <= max_rate:
		item2 = (float)(Ys[1])/(float)(i) + DP[i + Xs[1]]
	if i + Xs[2] <= max_rate:
		item3 = (float)(Ys[2])/(float)(i) + DP[i + Xs[2]]

	DP_path[i], DP[i] = min (enumerate([DP[i], item1, item2, item3]), key=itemgetter(1))
	if DP[i] == item1:
		if DP_path[i] is not 1:
			print "Error: 1"
	elif DP[i] == item2:
		if DP_path[i] is not 2:
			print "Error: 2"
	elif DP[i] == item3:
		if DP_path[i] is not 3:
			print "Error: 3"
			print DP[i]
			print DP_path[i]
			print DP[i], item1, item2, item3
	else:
		pass

final_path = []
path_index = 1
while path_index <= max_rate and DP_path[path_index] != 0:
	final_path.append(DP_path[path_index])
	path_index += Xs[DP_path[path_index]-1]

current_rate = 1
for p in xrange(len(final_path)-1):
	current_rate += Xs[final_path[p]-1]
	if final_path[p] < final_path[p+1]:
		pass
	if final_path[p] > final_path[p+1]:
		print "current rate: %s" % current_rate
		break



t12 = (Ys[1]-Ys[0]) / ( (Ys[0]/Xs[0])-(Ys[1]/Xs[1]) ) 
t23 = (Ys[2]-Ys[1]) / ( (Ys[1]/Xs[1])-(Ys[2]/Xs[2]) ) 


print final_path
print [i-1 for i in final_path]
print DP[1]



