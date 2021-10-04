from random import randint

def recursive(s, n, w):
    if n <= 1: return 0
    elif s[n - 1].peso > w: return recursive(s, n - 1, w)
    else: return max(recursive(s, n - 1, w), s[n - 1].valor + recursive(s, n - 1, w - s[n - 1].peso))

def aux_memoized(s, n, w, count=True, c=[0]):
    m = [[-1 for i in range(n + 2)] for j in range(w + 2)]
    r = memoized(s,n,w,m, count, c)
    # printMatrix(m)
    return r
# c = 0
def memoized(s, n, w, m, count=True, c=[0]):
    c[0] += 1
    if n <= 1: return 0
    if m[w][n] != -1:
        if count: c[0] -= 1
        return m[w][n]
    if s[n - 1].peso > w:
        m[w][n] = memoized(s, n - 1, w, m, count, c)
        return m[w][n]
    else:
        m[w][n] = max(memoized(s, n - 1, w, m, count, c), s[n - 1].valor + memoized(s, n - 1, w - s[n - 1].peso, m, count, c))
        return m[w][n]

def memoized_with_d(s, n, w, m=dict(), count=True, c=[0]):
    c[0] += 1
    if n <= 1: return 0
    rid = '{},{}'.format(w,n)
    if m.get(rid):
        if count: c[0] -= 1
        return m[rid]
    if s[n - 1].peso > w:
        m[rid] = memoized_with_d(s, n - 1, w, m, count, c)
        return m[rid]
    else:
        m[rid] = max(memoized_with_d(s, n - 1, w, m, count, c), s[n - 1].valor + memoized_with_d(s, n - 1, w - s[n - 1].peso, m, count, c))
        return m[rid]

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

    c1 = [0]
    found_m = aux_memoized(s, n + 1, w, True, c1)
    c1 = c1[0]
    c2 = [0]
    test = aux_memoized(s, n + 1, w, False, c2)
    c2 = c2[0]
    c3 = [0]
    d = dict()
    test1 = memoized_with_d(s,n + 1,w,d,True, c3)
    c3 = c3[0]
    print('m, !m, !m - m, d == {}, {}, {}, {}'.format(c1, c2, c2 - c1, c3))
    # print(d)
    expected, found_r = dynamicPrograming(s, n, w), recursive(s, n + 1, w)
    if not expected == found_r == found_m == test == test1:
        # print('{} | {} | {} | {} | {}'.format(expected, found_r, found_m, test, test1))
        print('WRONG')
        break
    # print('{} == {} == {} == {} == {}'.format(expected, found_r, found_m, test, test1))
