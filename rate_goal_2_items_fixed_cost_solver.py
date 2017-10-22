from __future__ import division
import math
import numpy as np

# R is fixed.
R = 120021
Xs = [10, 100]
Ys = [72, 110]

current_rate = 0

max_num = (R + max(Ys))
answers = [0 for i in xrange(max_num)]
choices = [0 for i in xrange(max_num)]
print max(Ys)
for i in xrange(R-1, 0, -1):
	answers[i] = np.min([answers[i+Xs[0]] + Ys[0]/i, answers[i+Xs[1]] + Ys[1]/i])
	choices[i] = np.argmin([answers[i+Xs[0]] + Ys[0]/i, answers[i+Xs[1]] + Ys[1]/i])

path = []
path_index = 1
while path_index < R:
	next_choice = choices[path_index]
	print path_index
	path_index += Xs[next_choice]
	path.append(next_choice)

print path