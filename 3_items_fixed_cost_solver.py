from __future__ import division
import math
import random
from operator import itemgetter

# M is fixed.

# M = 60000
# Xs = [10, 100, 300]
# Ys = [72.0, 700.0, 2050.0]
M = 9000
Xs = [5, 105, 1]
Ys = [10.0, 200.0, 2000.0]

# Went up to M = 4971672 - nothing...


# f = max(2, 2 * (float)(1)/(float)(Xs[2]) * (float)(Ys[2]+Ys[3]) / ( ((float)(Ys[2])/(float)(Xs[2]))-((float)(Ys[3])/(float)(Xs[3])) )  )
# minM = (f+2) * Ys[2]

# if M < minM:
# 	print "Goal %s is too small, it should be at least %s" % (M, minM)

# def should_buy(M, y, G, x):
# 	return M/G >= y/G + M/(G+x)

# M += 1
# Ys[1] = random.randint(20, 24) + random.random()
# Ys[2] = random.randint(85, 104) + random.random()
# if M > 25000:
# 	break
# print M, Ys[1], Ys[2]
max_rate = (int) (M * max((float)(x)/(float)(y) for (x,y) in zip (Xs, Ys)))
# print max_rate
# DP[i] represents best time needed starting from a rate of i
# DP_path[i] represents what to buy at time step i to get to optimal solution. 0 means no item,
# while 1, 2, 3 correspond to the items
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
	# item4 = DP[i]+1

	if i + Xs[0] <= max_rate:
		item1 = (float)(Ys[0])/(float)(i) + DP[i + Xs[0]]
	if i + Xs[1] <= max_rate:
		item2 = (float)(Ys[1])/(float)(i) + DP[i + Xs[1]]
	if i + Xs[2] <= max_rate:
		item3 = (float)(Ys[2])/(float)(i) + DP[i + Xs[2]]
	# if i + Xs[3] <= max_rate:
	# 	item4 = (float)(Ys[3])/(float)(i) + DP[i + Xs[3]]

	DP_path[i], DP[i] = min (enumerate([DP[i], item1, item2, item3]), key=itemgetter(1))
	# DP[i] = min (DP[i], item1, item2, item3, item4)
	if DP[i] == item1:
		if DP_path[i] is not 1:
			print "SOMETHING IS REALLY BAD 1"
			# print DP[i]
			# print DP_path[i]
			# print DP[i], item1, item2, item3

	elif DP[i] == item2:
		if DP_path[i] is not 2:
			print "SOMETHING IS REALLY BAD 2"
			# print DP[i]
			# print DP_path[i]
			# print DP[i], item1, item2, item3

	elif DP[i] == item3:
		if DP_path[i] is not 3:
			print "SOMETHING IS REALLY BAD 3"
			print DP[i]
			print DP_path[i]
			print DP[i], item1, item2, item3
	# elif DP[i] == item4:
	# 	DP_path[i] = 4
	else:
		pass

# print DP[1]
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
		# print "o m g %s" % p
		# print "total rate: %s" % current_rate
	if final_path[p] > final_path[p+1]:
		print "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOOO\n %s" % p
		print "current rate: %s" % current_rate
		break



t12 = (Ys[1]-Ys[0]) / ( (Ys[0]/Xs[0])-(Ys[1]/Xs[1]) ) 
t23 = (Ys[2]-Ys[1]) / ( (Ys[1]/Xs[1])-(Ys[2]/Xs[2]) ) 
# t34 = (Ys[3]-Ys[2]) / ( (Ys[2]/Xs[2])-(Ys[3]/Xs[3]) ) 

# print t12/2.0
# print t23/2.0
# print t34/2.0

# for p in xrange(len(DP_path)-1):
# 	if DP_path[p] < DP_path[p+1] and p != 0:
# 		print "DP path flipping point %s" % p
# 	if DP_path[p] > DP_path[p+1] and DP_path[p+1] != 0:
# 		print "Whoa (unflipping point) %s" % p


# print t13 
print final_path
print [i-1 for i in final_path]
print DP[1]
shifted_final_path = [i-1 for i in final_path]
# print shifted_final_path
# print DP[1]
if sorted(shifted_final_path) != shifted_final_path:
	print "WHOAAA!!"
	print shifted_final_path

