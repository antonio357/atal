from random import randint
#from sys import a

def cut_rod(p, n):
    if n == 0:
        return 0
    q = 0
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q

def iteractive_bottomUp_cutRod(prices, rod_len):
    previous_prices, biggest_price = [0] * (rod_len + 1), 0
    for rl in range(1, rod_len + 1):
        for rl_slice in range(1, rl+1):
            biggest_price = max(biggest_price, prices[rl_slice] + previous_prices[rl - rl_slice])
        previous_prices[rl] = biggest_price
    return biggest_price


for l in range(21):
    p = dict()
    for i in range(1, 51):
        p[i] = randint(5, 10)
    expected, found = cut_rod(p, l), iteractive_bottomUp_cutRod(p, l)
    if not expected == found:
        print('WRONG')
        break
    print('{} == {}'.format(expected, found))
