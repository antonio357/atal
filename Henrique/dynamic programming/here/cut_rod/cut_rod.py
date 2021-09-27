from random import randint
#from sys import a

def cut_rod(p, n):
    if n == 0:
        return 0
    q = 0
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q

p = dict()

for i in range(1, 51):
     p[i] = randint(5, 10)

print(cut_rod(p, 30))