from __future__ import division
import math
import random
import numpy as np


# Example with pre-computed OPT
M = 60000
Xs = [10, 100, 300]
Ys = [72.0, 700.0, 2050.0]
As = [1, 1, 1]
starting_cookies = 0
OPT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

MAX_REPEATS = 10000
MAX_TRIM_REPEATS = 10


NUM_OPERATIONS = 6
NUM_ITEMS = len(Xs)

def random_local_optimize(solution):
	op = random.randint(1, NUM_OPERATIONS)
	# print "Chose operation %s" % (op)
	if op == 1:
		# Add to some index
		index = random.randint(0, len(solution))
		item = random.randint(0, NUM_ITEMS-1)
		if should_add_to_index(solution, item, index):
			solution.insert(index, item)
	elif op == 2:
		# Delete from some index
		index = random.randint(0, len(solution)-1)
		if should_delete_from_index(solution, index):
			solution.pop(index)
	elif op == 3:
		# Move i to j. If j = i+1, equivalent to swap-consecutive.
		i = random.randint(0, len(solution) - 1)
		j = random.randint(0, len(solution) - 1)
		if should_move(solution, i, j):
			val = solution.pop(i)
			solution.insert(j, val)
	elif op == 4:
		# Replace value in i
		i = random.randint(1, len(solution)) - 1
		new_item = random.randint(0, NUM_ITEMS-1)
		if should_replace(solution, i, new_item):
			solution[i] = new_item
	elif op == 5:
		# Swap i and j
		i = random.randint(0, len(solution) - 1)
		j = random.randint(0, len(solution) - 1)
		if should_swap(solution, i, j):
			temp = solution[i]
			solution[i] = solution[j]
			solution[j] = temp
	else:
		# print 'trying to sort'
		if should_sort(solution):
			# print 'should sort! But not actually sorting'
			pass
			# solution.sort()

# Returns False if any swaps can improve, True if no swaps can improve
def no_swaps_can_improve(solution):
	for i in xrange(len(solution)):
		for j in xrange(len(solution)):
			if should_swap(solution, i, j):
				print 'should swap %s, %s' % (i, j)
				return False
	return True

# Returns False if any swaps can improve, True if no swaps can improve
def no_consecutive_swaps_can_improve(solution):
	for i in xrange(len(solution)):
		if should_swap_consecutive(solution, i):
			print 'should swap consecutive %s, %s' % (i, i+1)
			return False
	return True




# Tells you if you are at a local opt.
def local_optimize_exhaustive(solution):

	# Delete index
	for del_index in xrange(len(solution)):
		if should_delete_from_index(solution, del_index):
			print 'should del %s' % (del_index)
			return False

	# For each pair of indices, test if can do move
	for i in xrange(len(solution)):
		for j in xrange(len(solution)):
			if should_move(solution, i, j):
				print 'should swap %s, %s' % (i, j)
				return False

	# Test sorting
	if should_sort(solution):
		print 'should sort!'
		return False

	for item in xrange(NUM_ITEMS):
		# Add to index
		for add_index in xrange(len(solution) + 1):
			if should_add_to_index(solution, item, add_index):
				print 'should add %s' % (add_index)
				return False
		
		# For each index, try to replace value at index
		for i in xrange(len(solution)):
			if should_replace(solution, i, item):
				print 'should replace %s' % (i)
				return False
	
	return True


def random_trim(solution):
	# Delete from beginning/end
	begin_end = random.randint(0, 1)
	if begin_end:
		# Try to delete from beginning
		if should_delete_from_beginning(solution):
			solution.pop(0)
	else:
		# Try to delete from end
		if should_delete_from_end(solution):
			solution.pop()

def random_add_to_end_limited_items(solution):
	# Add to beginning/end
	item = random.randint(0, NUM_ITEMS-2)
	# Try to add to end
	if should_add_to_end(solution, item):
		print 'Added item %s to end' % item
		solution.append(item)

def should_add_to_end(solution, val):
	return should_add_to_index(solution, val, len(solution))

def should_add_to_beginning(solution, val):
	return should_add_to_index(solution, val, 0)

def should_add_to_index(solution, val, index):
	alt_solution = solution[:]
	alt_solution.insert(index, val)
	return compute_value(alt_solution) < compute_value (solution)

def should_delete_from_end(solution):
	return should_delete_from_index(solution, len(solution)-1)

def should_delete_from_beginning(solution):
	return should_delete_from_index(solution, 0)

def should_delete_from_index(solution, index):
	alt_solution = solution[:]
	alt_solution.pop(index)
	return compute_value(alt_solution) < compute_value (solution)

def should_replace(solution, ind, val):
	alt_solution = solution[:]
	alt_solution[ind] = val
	return compute_value(alt_solution) < compute_value(solution)


def should_swap_consecutive(solution, i):
	return should_move(solution, i, i+1)

def should_swap(solution, i, j):
	alt_solution = solution[:]
	temp = alt_solution[i]
	alt_solution[i] = alt_solution[j]
	alt_solution[j] = temp
	return compute_value(alt_solution) < compute_value(solution)

# def should_swap_consecutive_should_move(solution, i):
# 	return should_move(solution, i, i+1)

def should_move(solution, i, j):
	alt_solution = solution[:]
	val = alt_solution.pop(i)
	alt_solution.insert(j, val)
	return compute_value(alt_solution) < compute_value(solution)

def should_sort(solution):
	alt_solution = solution[:]
	alt_solution = sorted(alt_solution)
	return compute_value(alt_solution) < compute_value(solution)

def compute_value(solution):
	total_time = 0;
	G = 1;
	costs = Ys[:]
	for i in xrange(len(solution)):
		item = solution[i]
		# print item
		total_time += (float) (costs[item]) / (float) (G)
		costs[item] *= As[item]
		G += Xs[item]
	total_time += (float) (M) / (float) (G)
	return total_time



def random_init():
	# Compute all maxes
	n = len(Xs)
	# Maxs = [0 for i in xrange(n)]
	Maxs_fixed_cost = [0 for i in xrange(n)]
	for i in xrange(n):
		# Maxs[i] = int(math.ceil(math.log(M/Ys[i])/math.log(As[i])))+1
		Maxs_fixed_cost[i] = int(math.ceil(M/Ys[i]))
	# sum_of_maxes = np.sum(Maxs)
	max_of_maxes = np.max(Maxs_fixed_cost)
	return [random.randint(0,n-1) for i in xrange(max_of_maxes)]

def bad_init():
	# Copy paste this one in.
	solution = OPT[:]
	counter = 0
	trim_ratio = 0.1
	trim_amount = random.randint( int(len(OPT) * trim_ratio/2.0), int(len(OPT) * trim_ratio) )
	for i in xrange(trim_amount):
		solution.pop()

	old_solution = solution[:]
	random_add_to_end_limited_items(solution)
	while solution != old_solution or counter < MAX_TRIM_REPEATS:
		if old_solution == solution:
			counter += 1
		else:
			counter = 0
		old_solution = solution[:]
		random_add_to_end_limited_items(solution)

	return solution

def main():

	# while True:



	# Random initialization
	initial_solution = random_init()
	# initial_solution = bad_init()
	# print 'Initial bad solution:\n%s' % initial_solution
	iters = 0
	counter = 0
	solution = initial_solution

	old_solution = solution[:]
	random_trim(solution)
	while solution != old_solution or counter < MAX_TRIM_REPEATS:
		if old_solution == solution:
			counter += 1
		else:
			counter = 0
		old_solution = solution[:]
		random_trim(solution)


	old_solution = solution[:]
	random_local_optimize(solution)
	while solution != old_solution or counter < MAX_REPEATS:

		iters = iters + 1
		if iters % 1000 == 0:
			pass

		if old_solution == solution:
			counter += 1
		else:
			# print solution
			counter = 0

		old_solution = solution[:]
		random_local_optimize(solution)

	if sorted(solution) != solution:
		print 'Not sorted solution!'
		print 'random local optimizations got here ', solution
		print 'speed of solution', compute_value(solution)
		if no_swaps_can_improve(solution):
			print "No swaps, but can improve it!"
			# break
	print solution

sol = main()
