from random import randint

def recursive(s, n, w):
    if n <= 1: return 0
    elif s[n - 1].peso > w: return recursive(s, n - 1, w)
    else: return max(recursive(s, n - 1, w), s[n - 1].valor + recursive(s, n - 1, w - s[n - 1].peso))

def aux_memoized(s, n, w, count=True, c=[0]):
    m = [[-1 for i in range(n + 2)] for j in range(w + 2)]
    return memoized(s,n,w,m, count, c)
# c = 0
def memoized(s, n, w, m, count=True, c=[0]):
    c[0] += 1
    if n <= 1: return 0
    if m[w][n] != -1:
        if count: c[0] -= 1
        return m[w][n]
    elif s[n - 1].peso > w:
        m[w][n] = memoized(s, n - 1, w, m, count, c)
        return m[w][n]
    else:
        m[w][n] = max(memoized(s, n - 1, w, m, count, c), s[n - 1].valor + memoized(s, n - 1, w - s[n - 1].peso, m, count, c))
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

for n in range(1, 63+1):
    s, sr, ws, vs, w = {}, {}, [], [], n
    for i in range(1, n+1):
        s[i] = item(randint(1, n), randint(1, n*2))
        sr[i - 1] = s[i]
    for k in s.keys():
        if k != 0:
            ws.append(s[k].peso)
            vs.append(s[k].valor)

    c = [0]
    found_m = aux_memoized(s, n + 1, w, True, c)
    c1 = c[0]
    c = [0]
    test = aux_memoized(s, n + 1, w, False, c)
    c2 = c[0]
    print('m, !m, !m - m == {}, {}, {}'.format(c1, c2, c2 - c1))
    expected, found_r = dynamicPrograming(s, n, w), recursive(s, n + 1, w)
    if not expected == found_r == found_m == test:
        # print('{} | {} | {} | {}'.format(expected, found_r, found_m, test))
        print('WRONG')
        brk = True
        break
    # print('{} == {} == {} == {}'.format(expected, found_r, found_m, test))
