from __future__ import division
import math
import numpy as np

# R is fixed.

R = 120021
Xs = [10, 100]
Ys = [72, 110]

# minM = max(4, 2 * Ys[0]/Xs[0] * (Ys[0]+Ys[1]) / ( (Ys[0]/Xs[0])-(Ys[1]/Xs[1]) )  )

# if M < minM:
# 	print "Goal %s is too small, it should be at least %s", (M, minM)

current_rate = 0



max_num = (R + max(Ys))
answers = [0 for i in xrange(max_num)]
choices = [0 for i in xrange(max_num)]
print max(Ys)
for i in xrange(R-1, 0, -1):
	# print i
	# print len(answers)
	# print i+Xs[0]
	# print answers[i+Xs[0]]
	# print Ys[0]/i
	# print i+Xs[1]
	# print answers[i+Xs[1]]
	# print Ys[1]/i
	# print answers[i+Xs[0]] + Ys[0]/i
	# print answers[i+Xs[1]] + Ys[1]/i
	answers[i] = np.min([answers[i+Xs[0]] + Ys[0]/i, answers[i+Xs[1]] + Ys[1]/i])
	choices[i] = np.argmin([answers[i+Xs[0]] + Ys[0]/i, answers[i+Xs[1]] + Ys[1]/i])

path = []
path_index = 1
while path_index < R:
	next_choice = choices[path_index]
	print path_index
	path_index += Xs[next_choice]
	path.append(next_choice)


# print answers
# print choices
print path