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

for i in range(1, tam+1):
     p[i] = randint(5, 10)

print(cut_rod_memoizado(p, tam))