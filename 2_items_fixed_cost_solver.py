from __future__ import division
import math


# Example problem
M = 60000
Xs = [10, 100]
Ys = [72, 700]

minM = max(4, 2 * Ys[0]/Xs[0] * (Ys[0]+Ys[1]) / ( (Ys[0]/Xs[0])-(Ys[1]/Xs[1]) )  )

if M < minM:
	print "Goal %s is too small, it should be at least %s", (M, minM)

current_cookies = 0

def should_buy(M, y, G, x):
	return M/G >= y/G + M/(G+x)

def efficiency(x, y, G):
	return x/y * G/(x+G)


max_num = (int) (math.floor(M/Ys[0] - 1/Xs[0]))
answers = [0 for i in xrange(max_num)]

for i in xrange(max_num):
	if i%100 == 0:
		print i
	n1 = 0
	n2 = 0
	rate = 1
	time = 0
	for j in xrange(i):
		time += Ys[0]/rate
		rate += Xs[0]
		n1 += 1
	while should_buy(M, Ys[1], rate, Xs[1]):
		time += Ys[1]/rate
		rate += Xs[1]
		n2 += 1
	time += M/rate
	answers[i] = [time, n1, n2]

import numpy as np
import pylab as p
arr = np.array(answers)
for i in xrange(len(arr)):
	if i > 0 and i+1 < len(arr):
		if (arr[i][0] < arr[i-1][0]) and (arr[i][0] < arr[i+1][0]):
			print "%s is a local minimum" % (arr[i][:])
			print "it is less than %s and %s" % (arr[i-1][:], arr[i+1][0])

p.plot(arr[10:,1], arr[10:, 0])
p.xlabel("Number of item 1 purchased")
p.ylabel("Time of optimal solution")
p.title("Number of item 1 purchased vs. time of optimal solution")
boundary_rate = ( Ys[1]-Ys[0] ) / ( (Ys[0]/Xs[0]) - (Ys[1]/Xs[1]) )
print "T is equal to %s" % (boundary_rate)

boundary_num_items = (boundary_rate - 1)/Xs[0]
print boundary_num_items
print sorted(answers)[:15]
p.show()
