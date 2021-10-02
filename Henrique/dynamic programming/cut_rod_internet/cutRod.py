# A Dynamic Programming solution for Rod cutting problem
INT_MIN = -32767

# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces
def cutRod(price, n):
	# print('cutRod')
	val = [0 for x in range(n+1)]
	val[0] = 0

	# Build the table val[] in bottom up manner and return
	# the last entry from the table
	# print('val =', val)
	for i in range(1, n+1):
		# print('i =', i)
		max_val = INT_MIN
		for j in range(i):
			# print('j =', j, end=' ')
			# print('price[j] =', price[j], end=' ')
			# print('val[i-j-1] =', val[i-j-1], end=' ')
			max_val = max(max_val, price[j] + val[i-j-1])
		# print()
		val[i] = max_val
		# print('val =', val)

	return val[n]

def iteractive_bottomUp_cutRod(price, rod_len):
	biggest_price = 0
	previous_prices = [0]
	for rl in range(1, rod_len + 1):
		for rl_slice in range(rl):
			biggest_price = max(biggest_price, price[rl_slice] + previous_prices[rl - rl_slice - 1])
		previous_prices.append(biggest_price)
	return biggest_price

# Driver program to test above functions
arr = [1, 5, 8, 9, 10, 17, 17, 20]
p = {}
for i in range(len(arr)):
	p[i] = arr[i]
size = len(arr)
size = 8
for size in range(len(arr)+1):
	print("Maximum Obtainable Value is " + str(cutRod(arr, size)))
	print('iteractive_bottomUp_cutRod =', iteractive_bottomUp_cutRod(p, size))

# This code is contributed by Bhavya Jain


# def cut_rod(p, n):
#     if n == 0:
#         return 0
#     q = 0
#     for i in range(1, n+1):
#         q = max(q, p[i] + cut_rod(p, n-i))
#     return q

# def cut_rod_bottom_up(p, n):
#     if n == 0:
#         return 0
#     q = 0
#     for i in range(n, 0, -1):
#         if p.get(i):
#             q = max(q, p[i] + cut_rod_bottom_up(p, n - i))
#     return q

# print('here 1 =', cut_rod(p, size))
# print('here 2 =', cut_rod_bottom_up(p, size))
