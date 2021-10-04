from random import randint

def recursive(s, n, w):
    if n <= 1: return 0
    elif s[n - 1].peso > w: return recursive(s, n - 1, w)
    else: return max(recursive(s, n - 1, w), s[n - 1].valor + recursive(s, n - 1, w - s[n - 1].peso))

def aux_memoized(s, n, w):
    m = [[-1 for i in range(n + 2)] for j in range(w + 2)]
    return memoized(s,n,w,m)
c = 0
def memoized(s, n, w, m):
    global c
    c += 1
    if n <= 1: return 0
    if m[w][n] != -1:
        c -= 1
        return m[w][n]
    elif s[n - 1].peso > w:
        m[w][n] = memoized(s, n - 1, w, m)
        return m[w][n]
    else:
        m[w][n] = max(memoized(s, n - 1, w, m), s[n - 1].valor + memoized(s, n - 1, w - s[n - 1].peso, m))
        return m[w][n]

def printMatrix(m):
    print()
    for i in m: print(i)

def initMatrix(m, n, w):
    for r in range(w + 1):
        m.append(list())
        for c in range(n + 1):
            m[r].append(0)

def dynamicPrograming(s, n, w):
    m = list()
    initMatrix(m, n, w)
    for i in range(1, n + 1):
        for w in range(1, w + 1):
            if s[i].peso > w: m[w][i] = m[w][i - 1]
            else: m[w][i] = max(m[w - s[i].peso][i - 1] + s[i].valor, m[w][i - 1])
    return m[w][n]

class item():
    def __init__(self, peso, valor):
        self.valor = valor
        self.peso = peso

def pac(s, w):
    # driver code
    val = [s[x].valor for x in s.keys()]
    wt = [s[x].peso for x in s.keys()]
    W = w
    n = len(val)

    # We initialize the matrix with -1 at first.
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    return knapsack(wt, val, W, n, t)
def knapsack(wt, val, W, n, t):
    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # choice diagram code
    if wt[n - 1] <= W:
        t[n][W] = max(
            val[n - 1] + knapsack(
                wt, val, W - wt[n - 1], n - 1, t),
            knapsack(wt, val, W, n - 1, t))
        return t[n][W]
    elif wt[n - 1] > W:
        t[n][W] = knapsack(wt, val, W, n - 1, t)
        return t[n][W]

for n in range(1, 63+1):
    s, sr, ws, vs, w = {}, {}, [], [], n
    for i in range(1, n+1):
        s[i] = item(randint(1, n), randint(1, n*2))
        sr[i - 1] = s[i]
    for k in s.keys():
        if k != 0:
            ws.append(s[k].peso)
            vs.append(s[k].valor)

    expected, found_r, found_m, test = dynamicPrograming(s, n, w), recursive(s, n + 1, w), aux_memoized(s, n + 1, w), pac(s, w)
    if not expected == found_r == found_m == test:
        print('{} | {} | {} | {}'.format(expected, found_r, found_m, test))
        print('WRONG')
        brk = True
        break
    print('{} == {} == {} == {}'.format(expected, found_r, found_m, test))
