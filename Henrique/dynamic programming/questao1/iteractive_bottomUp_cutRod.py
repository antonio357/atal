from random import randint

def iteractive_bottomUp_cutRod(prices, rod_len):
    previous_prices, biggest_price = [0] * (rod_len + 1), 0
    for rl in range(1, rod_len + 1):
        for rl_slice in range(1, rl+1):
            biggest_price = max(biggest_price, prices[rl_slice] + previous_prices[rl - rl_slice])
        previous_prices[rl] = biggest_price
    return biggest_price


prices = dict()
rod_len = 994
for i in range(1, rod_len + 1):
     prices[i] = randint(5, 10)

print(iteractive_bottomUp_cutRod(prices, rod_len))
