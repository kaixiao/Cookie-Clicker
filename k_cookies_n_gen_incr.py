from __future__ import division
import math
import numpy as np


# M is fixed.
# (x1, y1, a1) and (x2, y2, a2) are fixed.

# Just need to solve DP[p, q] where p is amount of generator 1, q is amount of generator 2,
# and DP[p, q] is the min time to reach M from 0 starting with p, q as the generators.
# p is upper bounded by log(M/y1) / log(a1)
# q is upper bounded by log(M/y2) / log(a2)



# M = 10000
# Xs = [10, 250.11, 4.37]
# Ys = [80, 800.85, 41]
# As = [1.1, 1.15, 1.12]
# starting_cookies = 5000

M = 100000
Xs = [10.0, 100.0]
Ys = [80.0, 800.0]
As = [1.1, 4.0/3.0]
starting_cookies = 0






# M = 100000
# Xs = [1, 10]
# Ys = [10, 80]
# As = [1.13, 1.1]


def update_square(DP, DP_path, index, leftover_cookies):
	rate = sum(x[0]*x[1] for x in zip(index, Xs))+1

	index_maxs = DP.shape-np.array(1)
	min_time = (M-leftover_cookies)/rate
	# DP_path[] = -1 means buy nothing
	min_path = -1

	for i in xrange(len(index)):
		# if index == (7, 0):
		# 	print "Wahooooo!"
		# 	print index
		# 	print i
		# 	print index[i]
		# 	print leftover_cookies
		# 	print rate
		if index[i] != index_maxs[i]:
			new_index = np.copy(index)
			new_index[i] += 1
			new_index = tuple(new_index)
			# print new_index
			total_time = max((Ys[i]*As[i]**index[i]-leftover_cookies)/rate, 0) + DP[new_index]
			# if index == (7, 0):
			# 	print i
			# 	print total_time
			if total_time < min_time:
				# if index == (7, 0):
				# 	print 'made it'
				# 	print i
				# 	print total_time
				min_time = total_time
				min_path = i

	DP[index] = min_time
	DP_path[index] = min_path

def fill_out_grid(DP, DP_path, starting_cookies = 0):
	ordered_indices = np.flipud(np.array([l for l in np.ndindex(DP.shape)]))
	initialize = True
	for index in ordered_indices:
		index = tuple(index)
		cost = 0
		for i in xrange(len(index)):
			for j in xrange(index[i]):
				cost += Ys[i]*As[i]**j
		leftover_cookies = max(0, starting_cookies-cost)

		# For the very first index
		if initialize:
			rate = sum(x[0]*x[1] for x in zip(index, Xs))+1
			DP[index] = (M-leftover_cookies)/rate
			DP_path[index] = -1
			initialize = False
		else:
			update_square(DP, DP_path, index, leftover_cookies)

n = len(Xs)
Maxs = [0 for i in xrange(n)]
for i in xrange(n):
	Maxs[i] = int(math.ceil(math.log(M/Ys[i])/math.log(As[i])))+1
DP = np.empty((Maxs))
DP_path = np.empty((Maxs), dtype=int)


fill_out_grid(DP, DP_path, starting_cookies)



print DP
print DP_path




# ----------- Extra stuff ---------- #

# Uncomment to see 2D rates/efficiency grids (ONLY WORKS FOR 2D)
rates_grid = np.empty((Maxs))
efficiency_grid = np.empty((Maxs), dtype = int)
indices = np.array([l for l in np.ndindex(rates_grid.shape)])
def efficiency(x, y, G):
	return x/y * G/(x+G)

for index in indices:
	index = tuple(index)
	rates_grid[index] = sum(x[0]*x[1] for x in zip(index, Xs))+1
	if efficiency(Xs[0], Ys[0]*(As[0]**index[0]), rates_grid[index]) > \
	   efficiency(Xs[1], Ys[1]*(As[1]**index[1]), rates_grid[index]):
		efficiency_grid[index] = 0
	else:
		efficiency_grid[index] = 1

# print rates_grid
print efficiency_grid





path = []
path_efficiencies = []
normalized_path_efficiencies = []
efficient_choices = []
generators = [0 for i in xrange(n)]
gens_tuple = tuple(generators)
while DP_path[gens_tuple] != -1:
	path.append(DP_path[gens_tuple])
	rate = sum(x[0] * x[1] for x in zip(generators, Xs)) + 1
	efficiencies = [0 for i in xrange(n)]
	for i in xrange(n):
		efficiencies[i] = (Xs[i]/(Ys[i]*(As[i]**generators[i]))) * rate/(Xs[i]+rate)
	temp_min = min(efficiencies)
	normalized_path_efficiencies.append([int(100*i/temp_min)/100 for i in efficiencies])
	path_efficiencies.append(efficiencies)
	efficient_choices.append(np.argmax(efficiencies))
	generators[DP_path[gens_tuple]] += 1
	gens_tuple = tuple(generators)

print path
print normalized_path_efficiencies

eff_decisions_counter = 0

for i in xrange(len(path)):
	if (path[i] == efficient_choices[i]):
		eff_decisions_counter += 1
		# print 'TRUE'
	else:
		print i
		pass
		# print 'FALSE'
	# print path[i]
	# print path_efficiencies[i]

print eff_decisions_counter/len(path)

print DP[0][0]

