from __future__ import division
import math


# M is fixed.

M = 1000000
Xs = [100, 10]
Ys = [800, 80]
As = [1.4, 2]
starting_cookies = 1000



current_cookies = starting_cookies

def should_buy(M, m, y, G, x):
	if m < y:
		return (M-m)/G >= (y-m)/G + M/(G+x)
	else:
		return (M-m)/G >= (M-m+y)/(G+x)

def efficiency(x, y, G):
	return x/y * G/(x+G)

def efficiency_comparison_1(k, A, y1, y2):
	return y1 < y2*k

def efficiency_comparison_2(k, A, y1, y2):
	return y1*(A-1) < y2*(A**k-1)


def efficient_choice(m, x1, x2, y1, y2, A, G):
	# Assumption: y1 > y2
	# Which efficiency metric to use in region m > y1
	efficiency_comparison = efficiency_comparison_1
	if m < y2:
		if efficiency(x1, y1, G) > efficiency(x2, y2, G):
			return 0
		else:
			return 1
	elif m < y1:
		if (y1-m)/G + y2/(G+x2) < (y1+y2-m)/(G+x2):
			return 0
		else:
			return 1
	else:
		k = x1/x2
		if efficiency_comparison(k, A, y1, y2):
			return 0
		else:
			return 1

gen1 = 0
gen2 = 0
time_needed = 0
path = []



G = 1
x1 = 0
x2 = 0
y1 = 0
y2 = 0
buy_first_item = True

while should_buy(M, current_cookies, Ys[0]*(As[0]**gen1), G, Xs[0]) or \
	  should_buy(M, current_cookies, Ys[1]*(As[1]**gen2), G, Xs[1]):
	if Ys[0]*(As[0]**gen1) > Ys[1]*(As[1]**gen2):
		# Make y1 the bigger one
		x1 = Xs[0]
		y1 = Ys[0]*(As[0]**gen1)
		x2 = Xs[1]
		y2 = Ys[1]*(As[1]**gen2)
		A = As[1]
		buy_first_item = (efficient_choice(current_cookies, x1, x2, y1, y2, A, G) == 0)
	else:
		x1 = Xs[1]
		y1 = Ys[1]*(As[1]**gen2)
		x2 = Xs[0]
		y2 = Ys[0]*(As[0]**gen1)
		A = As[0]
		buy_first_item = (efficient_choice(current_cookies, x1, x2, y1, y2, A, G) == 1)
	#Uncomment next 4 to do conventional efficiency
	# if efficiency(Xs[0], Ys[0]*(As[0]**gen1), G) > efficiency(Xs[1], Ys[1]*(As[1]**gen2), G):
	# 	buy_first_item = True
	# else:
	# 	buy_first_item = False

	if buy_first_item:
		cookies_needed = max(0, Ys[0]*(As[0]**gen1)-current_cookies)
		current_cookies = current_cookies + cookies_needed - Ys[0]*(As[0]**gen1)
		time_needed += cookies_needed/G
		G += Xs[0]
		gen1 += 1
		path.append(0)
	else:
		cookies_needed = max(0, Ys[1]*(As[1]**gen2)-current_cookies)
		current_cookies = current_cookies + cookies_needed - Ys[1]*(As[1]**gen2)
		time_needed += cookies_needed/G
		G += Xs[1]
		gen2 += 1
		path.append(1)

time_needed += (M-current_cookies)/G


print time_needed
print path


