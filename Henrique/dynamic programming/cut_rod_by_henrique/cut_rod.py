from random import randint
#from sys import a

def cut_rod(p, n):
    if n == 0:
        return 0
    q = 0
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q

def cut_rod_bottom_up(p, n):
    if n == 0:
        return 0
    q = 0
    for i in range(n, 0, -1):
        q = max(q, p[i] + cut_rod_bottom_up(p, n - i))
    return q

print('mine == expected')
for i in range(10):
    p = dict()
    for i in range(1, 51):
         p[i] = randint(5, 100)
    mine = cut_rod_bottom_up(p, 20)
    expected = cut_rod(p, 20)
    # if mine != expected:
    #     print("wrong")
    #     break
    print('{} == {}'.format(mine, expected))

# p = dict()
# for i in range(1, 20):
#      p[i] = randint(5, 1000)
# print(cut_rod(p, len(p.keys())))
