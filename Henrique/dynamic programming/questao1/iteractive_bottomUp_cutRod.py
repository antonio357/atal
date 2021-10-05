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

def iteractive_bottomUp_cutRod(prices, rod_len):
    previous_prices, biggest_price = [0] * (rod_len + 1), 0
    for rl in range(1, rod_len + 1):
        for rl_slice in range(1, rl+1):
            biggest_price = max(biggest_price, prices[rl_slice] + previous_prices[rl - rl_slice])
        previous_prices[rl] = biggest_price
    return biggest_price


for l in range(973, 995):
    p = dict()
    l = 994
    for i in range(1, l+1):
        p[i] = randint(5, 10)
    expected, found = cut_rod_memoizado(p, l), iteractive_bottomUp_cutRod(p, l)
    if not expected == found:
        print('WRONG')
        break
    print('{} == {}'.format(expected, found))
