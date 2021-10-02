from random import randint
from sys import maxsize as inf

def cut_rod_memoizado(p, n):
    r = {}
    r[0] = 0
    for i in range(1, n + 1):
        r[i] = -inf
    return cut_rod_memoizado_aux(p, n, r)

def cut_rod_memoizado_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    else:
        q = 0
        for i in range(1, n+1):
            q = max(q, p[i] + cut_rod_memoizado_aux(p, n-i, r))
        r[n] = q
        return q


p = dict()

tam = 994

for i in range(1, tam + 1):
     p[i] = randint(5, 10)

print(cut_rod_memoizado(p, tam))

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

arr = [x for x in p.values()]
print(cutRod(arr, tam))


def iteractive_bottomUp_cutRod(price, rod_len):
    previous_prices, biggest_price = [0] * (rod_len + 1), 0
    for rl in range(1, rod_len + 1):
        for rl_slice in range(rl):
            biggest_price = max(biggest_price, price[rl_slice] + previous_prices[rl - rl_slice - 1])
        previous_prices[rl] = biggest_price
    return previous_prices[-1]

arr1 = []
for k in p.keys():
    arr1.append(p[k])
p1 = {}
for a in range(len(arr1)): p1[a] = arr1[a]

print(iteractive_bottomUp_cutRod(arr1, tam))
print(iteractive_bottomUp_cutRod(p1, tam))

# for i in range(len(arr)):
#     print('{} = {}'.format(i, arr[i]))
# print(p)

# def f(p, n):
#     r, s = [0] * (n), [0] * (n)
#     for j in range(1, n):
#         q = -123098
#         for i in range(1, j):
#             if q < p[i] + r[j - i]:
#                 q = p[i] + r[j - i]
#                 s[j] = i
#         r[j] = q
#     return r, s
# r, s = f(arr, len(arr))
# n = len(arr)
# while n > 0:
#     print(s[n])
#     n = n - s[n]
# print(n)
# print(r)
# print(s)


# def cut_rod(p, n):
#     if n == 0:
#         return 0
#     q = 0
#     for i in range(1, n+1):
#         q = max(q, p[i] + cut_rod(p, n-i))
#     return q
#
# print(cut_rod(p, tam))

